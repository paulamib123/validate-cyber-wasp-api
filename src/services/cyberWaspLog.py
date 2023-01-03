from typing import Dict, List
import logging

from src.models.CyberwaspLog import CyberwaspLogs

class CyberWaspLog():

    def __init__(self, log: Dict[str, str]):
        self.dateandtime = log.get("@timestamp")
        self.clientIp = log.get("client_ip")
        self.ruleId = log.get("rule_id")
        self.errorMsg = log.get("error_msg")
        self.stream = log.get("stream")
        self.attackURL = log.get("attack_url")
        self.eventTime = log.get("event_time")
        self.agent = log.get("agent")
        self.agentEphemeralID = self.agent.get("ephemeral_id")
        self.agentType = self.agent.get("type")
        self.agentID = self.agent.get("id")
        self.agentName = self.agent.get("name")
        self.agentVersion = self.agent.get("version")
        self.host = log.get("host")
        self.hostName = self.host.get("name")
        self.event = log.get("event")
        self.hostIP = log.get("host_ip")
        self.alertMsg = log.get("alert_msg")

    
    def setEmptyToNull(self, key, log):
        value = log.get(key)
        return None if not value else value

    def createDBObject(self, jsonData):
        
        CyberwaspLog = CyberwaspLogs(
            dateandtime = self.dateandtime,
            client_ip = self.clientIp,
            rule_id = self.ruleId, 
            error_msg = self.errorMsg, 
            stream = self.stream,
            attack_url = self.attackURL, 
            event_time = self.eventTime, 
            agent_ephemeral_id = self.agentEphemeralID,  
            agent_type = self.agentType,  
            agent_id = self.agentID, 
            agent_name = self.agentName, 
            agent_version = self.agentVersion,  
            host_name = self.hostName,  
            event = self.event, 
            host_ip = self.hostIP, 
            alert_msg = self.alertMsg 
        )
        
        logging.debug("Created Cyber Wasp Log Object for database")

        return CyberwaspLog


def postCyberWaspLogToDB(deviceData, Session):

    cyberWaspLog = CyberWaspLog(deviceData)

    logDBObject = cyberWaspLog.createDBObject(deviceData)
    
    session = Session()

    session.add(logDBObject)
    logging.info("Added Cyber Wasp Log with Client IP Address {} to database".format(cyberWaspLog.clientIp))

    session.commit()
    logging.info("Committed Cyber Wasp Log with Client IP Address {} to database".format(cyberWaspLog.clientIp))

    
