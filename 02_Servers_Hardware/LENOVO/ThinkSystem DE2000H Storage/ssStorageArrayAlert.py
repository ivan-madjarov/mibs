# CSA AI 48562
try:
    evt.eventKey = evt.ssEventType
    evt.component = evt.ssEventComponentType + " [" + evt.ssEventComponentLocation + "]"
    ssEventPriorityNumeric = {"Critical": 5, "Warning": 3, "Informational": 2}
    evt.severity = ssEventPriorityNumeric[evt.ssEventPriority]
    evt.message = "Alarm on " + evt.ssStorageArrayName + " [" + evt.ssNetworkNodeName + "]: " + evt.ssEventDescription
    evt.summary = evt.message
except:
    pass