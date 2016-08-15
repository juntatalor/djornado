#!/usr/bin/env bash

function startup()
{
    # postgreSQL
    sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

    apt-get update -y
}

### START setup-apt.sh
function apt-install {
    for pkg in $@; do
        echo -e "[APT-GET] Installing package $pkg..."
        sudo apt-get install -yq $pkg
    done
}


function apt-install-if-needed {
    for pkg in $@; do
        if package-not-installed $pkg; then
            apt-install $pkg
        fi
    done
}


function package-not-installed {
    test -z "$(sudo dpkg -s $1 2> /dev/null | grep Status)"
}

### END setup-apt.sh

PROJECT_HOME='/home/vagrant'
PRJ_NAME=$1
OS_REQUIREMENTS_FILENAME="$PROJECT_HOME/$PRJ_NAME/requirements/requirements.apt"


function list_packages(){
    cat ${OS_REQUIREMENTS_FILENAME} | grep -v "#" | grep -v "^$";
}


function install_os_dependencies()
{
    list_packages | xargs apt-get --no-upgrade install -y;
}


function install_postgresql()
{
    PG_VERSION="9.5"
    PG_CONF="/etc/postgresql/$PG_VERSION/main/postgresql.conf"
    PG_HBA="/etc/postgresql/$PG_VERSION/main/pg_hba.conf"
    PG_DIR="/var/lib/postgresql/$PG_VERSION/main"

    APP_DB_USER=vagrant
    APP_DB_PASS=dbpass
    APP_DB_NAME="$PRJ_NAME"_db

    apt-install-if-needed "postgresql-$PG_VERSION" "postgresql-contrib-$PG_VERSION" "postgresql-server-dev-$PG_VERSION"

    # Edit postgresql.conf to change listen address to '*':
    sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/" "$PG_CONF"

    # Append to pg_hba.conf to add password auth:
    echo "host    all             all             all                     md5" >> "$PG_HBA"

    # Restart so that all new config is loaded:
    service postgresql restart

    cat << EOF | su - postgres -c psql
    -- Create the database user:
    CREATE USER $APP_DB_USER
        WITH PASSWORD '$APP_DB_PASS' SUPERUSER CREATEDB;

    -- Create the database:
    CREATE DATABASE $APP_DB_NAME
        WITH OWNER $APP_DB_USER
        TEMPLATE=template0
        ENCODING = 'UTF-8'
        LC_COLLATE = 'en_US.UTF-8'
        LC_CTYPE = 'en_US.UTF-8';
EOF
}


function install_python()
{
    PY_VERSION="3.5.1"
    PY_NAME="Python-$PY_VERSION"
    cd /tmp
    echo "[DOWNLOAD] $PY_NAME"
    wget -q http://www.python.org/ftp/python/$PY_VERSION/$PY_NAME.tar.xz
    tar xJf $PY_NAME.tar.xz; cd $PY_NAME
    ./configure --prefix=/opt/python3
    make
    make install

    rm -rf $PY_NAME*
    cd -

    VIRTUALENV_PATH="$PROJECT_HOME/$PRJ_NAME/.env"
    su -l vagrant -c "/opt/python3/bin/python3 -m venv $VIRTUALENV_PATH"
    echo -e "
    # virtualenv settings
    source $VIRTUALENV_PATH/bin/activate
    cd $PROJECT_HOME/$PRJ_NAME
    "  >> $PROJECT_HOME/.bashrc

    su -l vagrant -c "$VIRTUALENV_PATH/bin/python -m pip install -r $PROJECT_HOME/$PRJ_NAME/requirements/requirements.txt"
}

function install_protobuf()
{
    PROTO_VERSION="3.0.0"
    cd /tmp
    echo "[DOWNLOAD] Protobuf-$PROTO_VERSION"
    wget -q https://github.com/google/protobuf/archive/v$PROTO_VERSION.tar.gz
    tar -zxvf $PROTO_VERSION.tar.gz
    cd protobuf-$PROTO_VERSION
    sudo ./autogen.sh
    sudo ./configure
    sudo make
    sudo make check
    sudo make install clean
    sudo ldconfig
}


startup
install_os_dependencies
install_python
install_postgresql
install_protobuf