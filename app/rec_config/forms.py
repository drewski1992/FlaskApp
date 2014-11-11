"""
    rec_config.forms
    ~~~~~~~~~~~~~~~~

    Provide input forms for editing and creating configuations.
"""

# Python2.7 Imports
import time

# flask extensions
from flask_wtf import Form

# WTForms Imports
from wtforms import StringField, SubmitField, IntegerField, BooleanField
from wtforms.validators import Required, Length

# app imports
from app.models import Configuration, CurrentConfiguration



class ConfigurationNewForm(Form):
    """
        rec_config.forms.ConfigurationForm
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        So every form is defined individualy for ease.

    """
    # string_fields = StringField("IP 1a", validators=[Length(7,20)])
    # integer_fields = IntegerField("Port 1a")
    # bool_fields = BooleanField()
    # sfp_cage1 = {}
    # sfp_cage2 = {}
    # sfp_cage3 = {}
    # sfp_cage4 = {}
    config_name = StringField("Configuration Name", validators=[Required(), Length(1,120)])

    # SFP Cage 1
    ip_1a = StringField("IP 1a", validators=[Length(7,20)])
    ip_1b = StringField("IP 1b", validators=[Length(7,20)])
    ip_1c = StringField("IP 1c", validators=[Length(7,20)])
    ip_1d = StringField("IP 1d", validators=[Length(7,20)])

    port_1a = IntegerField("Port 1a")
    port_1b = IntegerField("Port 1a")
    port_1c = IntegerField("Port 1a")
    port_1d = IntegerField("Port 1a")

    enabled_1a = BooleanField()
    enabled_1b = BooleanField()
    enabled_1c = BooleanField()
    enabled_1d = BooleanField()

    # SFP Cage 2
    ip_2a = StringField("IP 1a", validators=[Length(7,20)])
    ip_2b = StringField("IP 1b", validators=[Length(7,20)])
    ip_2c = StringField("IP 1c", validators=[Length(7,20)])
    ip_2d = StringField("IP 1d", validators=[Length(7,20)])

    port_2a = IntegerField("Port 1a")
    port_2b = IntegerField("Port 1a")
    port_2c = IntegerField("Port 1a")
    port_2d = IntegerField("Port 1a")

    enabled_2a = BooleanField()
    enabled_2b = BooleanField()
    enabled_2c = BooleanField()
    enabled_2d = BooleanField()


    # SFP Cage 3
    ip_3a = StringField("IP 1a", validators=[Length(7,20)])
    ip_3b = StringField("IP 1b", validators=[Length(7,20)])
    ip_3c = StringField("IP 1c", validators=[Length(7,20)])
    ip_3d = StringField("IP 1d", validators=[Length(7,20)])

    port_3a = IntegerField("Port 1a")
    port_3b = IntegerField("Port 1a")
    port_3c = IntegerField("Port 1a")
    port_3d = IntegerField("Port 1a")

    enabled_3a = BooleanField()
    enabled_3b = BooleanField()
    enabled_3c = BooleanField()
    enabled_3d = BooleanField()


    # SFP Cage 4
    ip_4a = StringField("IP 1a", validators=[Length(7,20)])
    ip_4b = StringField("IP 1b", validators=[Length(7,20)])
    ip_4c = StringField("IP 1c", validators=[Length(7,20)])
    ip_4d = StringField("IP 1d", validators=[Length(7,20)])

    port_4a = IntegerField("Port 1a")
    port_4b = IntegerField("Port 1a")
    port_4c = IntegerField("Port 1a")
    port_4d = IntegerField("Port 1a")

    enabled_4a = BooleanField()
    enabled_4b = BooleanField()
    enabled_4c = BooleanField()
    enabled_4d = BooleanField()

    # sfp_cage1['ip'] = []
    # sfp_cage1['port'] = []
    # sfp_cage1['enabled'] = []
    # for num in range(0, 4):
    #     sfp_cage1['ip'].append(string_fields)
    #     sfp_cage1['port'].append(integer_fields)
    #     sfp_cage1['enabled'].append(bool_fields)

    # print sfp_cage1
    submit = SubmitField("Save Configuration")
