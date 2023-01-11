from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CyberwaspLogs(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    dateandtime = db.Column(db.DateTime())
    client_ip = db.Column(db.Text)
    rule_id = db.Column(db.Text)
    error_msg = db.Column(db.Text)
    stream = db.Column(db.Text)
    attack_url = db.Column(db.Text)
    event_time = db.Column(db.Text)
    agent_ephemeral_id = db.Column(db.Text)
    agent_type = db.Column(db.Text)
    agent_id = db.Column(db.Text)
    agent_name = db.Column(db.Text)
    agent_version = db.Column(db.Text)
    host_name = db.Column(db.Text)
    event = db.Column(db.JSON())
    host_ip = db.Column(db.Text)
    alert_msg = db.Column(db.TEXT())
    created_at = db.Column(db.DateTime())
