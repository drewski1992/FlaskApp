"""
    app.models
    ~~~~~~~~~~

    The description of the class elements and their
    components are used for creating and interfacing with the
    sqlite database.
"""


# Application Database
from app import db, login_manager

from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    """
    user_id             integer primary key autoincrement not null,
    name                text,
    password            text
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(120), unique=False)

    def __init__(self, name, password):
        self.name = name
        self.password_hash = generate_password_hash(password)

    def __repr__(self):
        return '<User %r>' % self.name

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Log(db.Model):
    """
    """
    log_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    level = db.Column(db.String(10), unique=False, nullable=False)
    date = db.Column(db.Integer, unique=True, nullable=False)
    message = db.Column(db.String(255), unique=False, nullable=False)
    action = db.Column(db.String(255), unique=False, nullable=False)

    def __init__(self, user_id, level, date, message, action):
        self.user_id = user_id
        self.level = level
        self.date = date
        self.message = message
        self.action = action

    def __repr__(self):
        return '<Log: {0}'.format(self.message)


class ServerStatus(db.Model):
    """
    server_id               integer primary key autoincrement not null,
    executing_bit           bool,
    recording               bool,
    config_active           bool,
    space_used              integer,
    space_avail             integer,
    space_fail              integer,
    opr_status              bool
    """
    server_id = db.Column(db.Integer, primary_key=True)
    executing_bit = db.Column(db.Boolean)
    recording = db.Column(db.Boolean)
    config_active = db.Column(db.Boolean)
    space_used = db.Column(db.Integer)
    space_fail = db.Column(db.Integer)
    space_avail = db.Column(db.Integer)
    opr_status = db.Column(db.Boolean)

    def __init__(self, executing_bit, recording, config_active, space_used,
                 space_fail, opr_status):
        self.executing_bit = executing_bit
        self.recording = recording
        self.config_active = config_active
        self.space_used = space_used
        self.space_fail = space_fail
        self.opr_status = opr_status

    def __repr__(self):
        return 'Executing Bit: {0}, Recording: {1}, Config Active: {2}, Space Used: {3}, Space Fail: {4}, OPR Status: {5}'.format(
            self.executing_bit, self.recording, self.config_active, self.space_used, self.space_fail, self.opr_status
        )

    # TODO Add methods for updating ServerStatus fields


class Recording(db.Model):
    """
    recID               integer primary key autoincrement not null,
    recName             text,
    label               text,
    recSize             integer,
    startTime           integer,
    endTime             integer
    user_id             integer
    foreign key(user_id) references User(user_id)
    """
    # TODO Come up with a better naming convention
    rec_id = db.Column(db.Integer, primary_key=True)
    rec_name = db.Column(db.String(120), nullable=False, unique=True)
    label = db.Column(db.String(120), nullable=False, unique=False)
    rec_size = db.Column(db.Integer, nullable=False, unique=False)
    start_time = db.Column(db.Integer, nullable=False, unique=False)
    end_time = db.Column(db.Integer, nullable=False, unique=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, rec_name, lable, rec_size, start_time, end_time):
        self.rec_name = rec_name
        self.label = lable
        self.rec_size = rec_size
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return 'Rec ID: {0}, Label: {1}, Rec Size: {2}, Start Time: {3}, End Time: {4}'.format(
            self.rec_id, self.label, self.rec_size, self.start_time, self.end_time
        )

    # TODO Add columns that hold the pointers the the first package in memory


class EventTag(db.Model):
    """
    TagID               integer primary key autoincrement not null,
    description         text,
    tagTime             integer,
    recordID            integer,
    foreign key(recordID) references Recording(recID)
    """
    # TODO Come up with a better naming convention
    tag_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    tag_time = db.Column(db.Integer, nullable=False)
    record_id = db.Column(db.Integer, db.ForeignKey('recording.rec_id'))

    def __init__(self, description, tag_time, record_id):
        self.description = description
        self.tag_time = tag_time
        self.record_id = record_id

    def __repr__(self):
        return 'Tag ID: {0}, Description: {1}, Tag Time: {2}, Record ID: {3}'.format(
            self.tag_id, self.description, self.tag_time, self.record_id
        )


class Configuration(db.Model):
    """
    configID            integer primary key autoincrement not null,
    configName          text,
    configTime          integer
    user_id             integer
    foreign key(user_id) references User(user_id)

    SFP Cages 1:4, UDP Channels a:h (ip->String(20), port->Integer)
    """
    config_id = db.Column(db.Integer, primary_key=True)
    config_name = db.Column(db.String(120), nullable=False)
    config_time = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # SFP Cage 1
    ip_1a = db.Column(db.String(20), nullable=True)
    ip_1b = db.Column(db.String(20), nullable=True)
    ip_1c = db.Column(db.String(20), nullable=True)
    ip_1d = db.Column(db.String(20), nullable=True)

    port_1a = db.Column(db.Integer, nullable=True)
    port_1b = db.Column(db.Integer, nullable=True)
    port_1c = db.Column(db.Integer, nullable=True)
    port_1d = db.Column(db.Integer, nullable=True)

    # SFP Cage 2
    ip_2a = db.Column(db.String(20), nullable=True)
    ip_2b = db.Column(db.String(20), nullable=True)
    ip_2c = db.Column(db.String(20), nullable=True)
    ip_2d = db.Column(db.String(20), nullable=True)

    port_2a = db.Column(db.Integer, nullable=True)
    port_2b = db.Column(db.Integer, nullable=True)
    port_2c = db.Column(db.Integer, nullable=True)
    port_2d = db.Column(db.Integer, nullable=True)

    # SFP Cage 3
    ip_3a = db.Column(db.String(20), nullable=True)
    ip_3b = db.Column(db.String(20), nullable=True)
    ip_3c = db.Column(db.String(20), nullable=True)
    ip_3d = db.Column(db.String(20), nullable=True)

    port_3a = db.Column(db.Integer, nullable=True)
    port_3b = db.Column(db.Integer, nullable=True)
    port_3c = db.Column(db.Integer, nullable=True)
    port_3d = db.Column(db.Integer, nullable=True)

    # SFP Cage 4
    ip_4a = db.Column(db.String(20), nullable=True)
    ip_4b = db.Column(db.String(20), nullable=True)
    ip_4c = db.Column(db.String(20), nullable=True)
    ip_4d = db.Column(db.String(20), nullable=True)

    port_4a = db.Column(db.Integer, nullable=True)
    port_4b = db.Column(db.Integer, nullable=True)
    port_4c = db.Column(db.Integer, nullable=True)
    port_4d = db.Column(db.Integer, nullable=True)

    # SFP Cage 5
    ip_5a = db.Column(db.String(20), nullable=True)
    ip_5b = db.Column(db.String(20), nullable=True)
    ip_5c = db.Column(db.String(20), nullable=True)
    ip_5d = db.Column(db.String(20), nullable=True)

    port_5a = db.Column(db.Integer, nullable=True)
    port_5b = db.Column(db.Integer, nullable=True)
    port_5c = db.Column(db.Integer, nullable=True)
    port_5d = db.Column(db.Integer, nullable=True)

    # SFP Cage 6
    ip_6a = db.Column(db.String(20), nullable=True)
    ip_6b = db.Column(db.String(20), nullable=True)
    ip_6c = db.Column(db.String(20), nullable=True)
    ip_6d = db.Column(db.String(20), nullable=True)

    port_6a = db.Column(db.Integer, nullable=True)
    port_6b = db.Column(db.Integer, nullable=True)
    port_6c = db.Column(db.Integer, nullable=True)
    port_6d = db.Column(db.Integer, nullable=True)

    # SFP Cage 7
    ip_7a = db.Column(db.String(20), nullable=True)
    ip_7b = db.Column(db.String(20), nullable=True)
    ip_7c = db.Column(db.String(20), nullable=True)
    ip_7d = db.Column(db.String(20), nullable=True)

    port_7a = db.Column(db.Integer, nullable=True)
    port_7b = db.Column(db.Integer, nullable=True)
    port_7c = db.Column(db.Integer, nullable=True)
    port_7d = db.Column(db.Integer, nullable=True)

    # SFP Cage 8
    ip_8a = db.Column(db.String(20), nullable=True)
    ip_8b = db.Column(db.String(20), nullable=True)
    ip_8c = db.Column(db.String(20), nullable=True)
    ip_8d = db.Column(db.String(20), nullable=True)

    port_8a = db.Column(db.Integer, nullable=True)
    port_8b = db.Column(db.Integer, nullable=True)
    port_8c = db.Column(db.Integer, nullable=True)
    port_8d = db.Column(db.Integer, nullable=True)

    def __init__(self, **kwargs):
        super(Configuration, self).__init__(**kwargs)

    def __repr__(self):
        return '<Configuration: {0}>'.format(self.config_name)

    # TODO Fix constructor to accept a list of details for an entire configuration file
    # TODO Add Methods to add details by SFP Cage


class CurrentConfiguration(db.Model):
    """
    curconfID           integer primary key autoincrement not null,
    configID            integer,
    foreign key(configID) references Configuration(configID)
    """
    current_config_id = db.Column(db.Integer, primary_key=True)
    config_id = db.Column(db.Integer, db.ForeignKey('configuration.config_id'))

    def __init__(self, config_id):
        self.config_id = config_id

    def __repr__(self):
        return 'Current Config ID: {0}, Config ID: {1}'.format(
            self.current_config_id, self.config_id
        )



#class ConfigFMCDetail(db.Model):
    """
    ConfigFMCDetailID   integer primary key autoincrement not null,
    configurationID     integer,
    foreign key(configurationID) references Configurations(configID)
    """


#class BuiltInTest(db.Model):
    """
    BITid               integer primary key autoincrement not null,
    BITtime             integer,
    errors              text
    """


#class BITStackDetail(db.Model):
    """
    stackDetailID       integer primary key autoincrement not null,
    stackNum            integer,
    temp                integer,
    memory              text,
    BuiltInTestID       integer,
    foreign key(BuiltInTestID) references BuiltInTest(BITid)
    """