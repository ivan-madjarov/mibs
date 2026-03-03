Readme.txt
 
-------------------------------------------------------------------
This file outlines changes since the last release of MIBs.
 
It is very strongly recommended that you load and compile ALL of
the MIBs provided.
 
Please load the 'hpicfOid.mib' before loading the other specific
MIBs.  This is due to the fact that the 'hpicfOid.mib' is the
parent MIB to most of the HP device specific MIBs.
-------------------------------------------------------------------
 
		hpicfAuth.mib
		   -new objects
			hpSwitchAuthAllowVlanTagged
		   -modified objects
                       hpicfSwitchBypassUsername  
 
 
		hpicfBridge.mib
		   -new objects
			hpicfBridgeStpBpduThrottleStatus
			hpicfBridgeStpBpduThrottleValue
 
 
		hpicfByod.mib
		 -new mib
 
 
		hpicfDhcpClient.mib
		   -new objects
			hpicfDhcpClientTR069AcsUrlOptionStatus
 
 
		hpicfDhcpv4Server.mib
		 -new mib
 
 
		hpicfDhcpv6Relay.mib
		   -new objects
			hpicfDhcpv6RelayOption79Status
 
 
		hpicfDot1x.mib
		   -new objects
			hpicfDot1xPaePortMBV
 
 
		hpicfDownload.mib
		   -new objects
			hpicfDownloadTftpClientConfig
 
 
		hpicfIpRoute.mib
		   -new objects
			hpicfIpv6RouteCnt
			hpicfIpv6RouteEntry
			hpicfIpv6RouteProto
			hpicfIpv6RouteSummaryTable
 
 
		hpicfOid.mib
		   -modified objects
                        hpStack
                        hpSwitch2510BPortSlot
                        hpSwitchJ9737APowerSupply
			hpSwitchJ9738APowerSupply
			hpSwitchJ4899B
			hpSwitchJ4900B
			hpSwitchJ9080A
			hpSwitchJ9085A
			hpSwitchJ9028B
			hpSwitchJ4900C
			hpSwitchJ9265A
			hpSwitchJ9263A
			hpSwitchJ9264A
		   -new objects
                        hpSwitchJL070A 
			hpSwitchModuleJL070A
 
		hpicfOspfv3.mib
		 -new mib
		
                hpicfSntp.mib
		   -modified objects
			hpSntpConfigMode
			hpTimeSyncMethod
 
                hpicfTR069.mib
	           -new mib
 
 
		hpicfUdld.mib
		   -new objects
			hpicfUdldConfigForwardMode
                        hpicfUdldConfigTimeIntervalMs 
 
 
		hpSwitchBasicConfig.mib
		   -new objects
			hpSwitchAclIpv4DenyFragmentedTcpHeader
			hpSwitchAclIpv6DenyNonClassifiableL4Header
 
 
		hpSwitchConfig.mib
		   -new objects
			hpSwitchTcpPushPreserveConfig
 
		hpSwitchTrap.mib
		   -new objects
                        hpSwitchJ9660Atrap  
			hpSwitchJ9800Atrap  
			hpSwitchJ9801Atrap  
			hpSwitch498358-B21trap   
			hpSwitch516733-B21trap   
			hpSwitchJ9780Atrap    
			hpSwitchJL070Atrap    

