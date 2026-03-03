Readme.txt
 
-------------------------------------------------------------------
This file outlines changes since the last release of MIBs.
 
It is very strongly recommended that you load and compile ALL of
the MIBs provided.
 
Please load the 'hpicfOid.mib' before loading the other specific
MIBs.  This is due to the fact that the 'hpicfOid.mib' is the
parent MIB to most of the HP device specific MIBs.
-------------------------------------------------------------------
 
		hpicfArpThrottle.mib
		 -new mib
 
 
		hpicfAuth.mib
		   -new objects
			hpicfSwitchOperatorPwdAgingInterval
			hpicfSwitchOperatorPwdLengthValue
			hpicfSwitchUserPwdAgingInterval
			hpicfSwitchUserPwdLengthValue
			hpSwitchAuthenCompositionIndex
			hpSwitchAuthenCompositionValue
			hpSwitchAuthPwdAgingCheck
			hpSwitchAuthPwdAgingValue
			hpSwitchAuthPwdAlertBeforeExpiry
			hpSwitchAuthPwdControlCheck
			hpSwitchAuthPwdExpiredUserLoginAttempts
			hpSwitchAuthPwdExpiredUserLoginDays
			hpSwitchAuthPwdHistoryCheck
			hpSwitchAuthPwdHistoryRecordsRange
			hpSwitchAuthPwdLogonDetailsCheck
			hpSwitchAuthPwdRepeatCharactersCheck
			hpSwitchAuthPwdRepeatPasswordCheck
			hpSwitchAuthPwdUpdateInterval
			hpSwitchAuthPwdUserNameCheck
			hpSwitchLocalMgmtPwdUserAgingInterval
			hpSwitchLocalMgmtPwdUserPasswdLengthValue
			hpSwitchRadiusTracking
			hpSwitchRadiusTrackingUserName
 
 
		hpicfBfd.mib
		 -new mib
 
 
		hpicfDevConf.mib
		 -new mib
 
 
		hpicfDhcpv4Server.mib
		   -new objects
			hpicfDhcpv4ServerOperStatus
 
 
		hpicfFf.mib
		   -modified objects
                        HpicfFaultType
		   -new objects
			hpicfFfLinkFlapControlAction
			hpicfFfLinkFlapControlPortDisableTimer
			hpicfFfLinkFlapControlPortIndex
			hpicfFfLinkFlapControlSensitivity
 
 
		hpicfGppcv2.mib
		   -new objects
			hpicfGppcv2AcSharedFlag
 
 
		hpicfJobScheduler.mib
		   -new objects
			hpicfJobSchedulerCount
			hpicfJobSchedulerDelay
			hpicfJobSchedulerStatus
 
 
		hpicfMdns.mib
		 -new mib
 
 
		hpicfMld.mib
		   -new objects
			hpicfMldReload
 
 
		hpicfMvrp.mib
		 -new mib
 
 
		hpicfNtp.mib
		 -new mib
 
 
		hpicfOid.mib
		   -new objects
			aruba3810
			arubaFPModuleJL078A
			arubaFPModuleJL079A
			arubaFPModuleJL083A
			arubaFPModule
			arubaJL071AModule
			arubaJL071A
			arubaJL072AModule
			arubaJL072A
			arubaJL073AModule
			arubaJL073A
			arubaJL074AModule
			arubaJL074A
			arubaJL075AModule
			arubaJL075A
			arubaJL076AModule
			arubaJL076A
			arubaJL084AStackingModule
			arubaJL085APowerSupply
			arubaJL086APowerSupply
			arubaJL087APowerSupply
			arubaJL088AFanTray
			arubaStack3810
			hpStackVSF5400R
 
 
		hpicfOspf.mib
		   -new objects
			hpicfOspfIfBfdEnbl
 
		hpicfPoe.mib
		   -new objects
			hpicfPoePethPsePortResetState
 
		hpicfPrivateVlan.mib
		 -new mib
 
		hpicfRateLimit.mib
		   -modified objects
			hpICMPRateLimitPortKbps
 
		hpicfRipng.mib
		 -new mib
 
 
		hpicfSntp.mib
		   -modified objects
			hpTimeSyncMethod
 
		hpicfSyslog.mib
		   -modified objects
			HpicfSyslogSystemModule
 
		hpicfUsrAuth.mib
		   -new objects
                        hpicfUsrAuthCaptivePortalConfigEnabled
                        hpicfUsrAuthCaptivePortalUrlHashKey
                        hpicfUsrAuthCaptivePortalUrlHashKeyEncrypted

		hpicfVrrpv3.mib
		   -new objects
			hpicfVrrpv3VrBfdIPAddr
 
		hpicfVsfVC.mib
		 -new mib
 
		hpSwitchBasicConfig.mib
		   -new objects
			hpSwitchAclGroupingEnable
			hpSwitchFPModuleConfigName
			hpSwitchFPModuleConfigType
			hpSwitchRESTInterfaceStatus
			hpSwitchRESTSessionIdleTimeout
 
 
		hpSwitchConfig.mib
		   -new objects
			hpicfPrivateVlanPromiscuousPorts
			hpSwitchPreviewMode
 
 
		hpSwitchTrap.mib
		   -new objects
			arubaJL071Atrap
			arubaJL072Atrap
			arubaJL073Atrap
			arubaJL074Atrap
			arubaJL075Atrap
			arubaJL076Atrap
			arubaStack3810trap
			hpStackVSF5400Rtrap
 
 
		ianabfdstd.mib
		 -new mib
 
		rfc5907.mib
		 -new mib
 
 
		rfc7330.mib
		 -new mib
 
 
		rfc7331.mib
		 -new mib
 
List of new traps supported in this release
-------------------------------------------

                hpicfArpThrottle.mib
		 -new Trap objects
                      hpicfArpthrottleExceedThresholdTrap

                hpicfAuth.mib
		 -new Trap objects
                      hpSwitchPasswordExpiryNotify  

                hpicfVsfVC.mib
		 -new Trap objects
                      hpicfVsfVCCommanderChange
                      hpicfVsfVCMemberChange
                      hpicfVsfVCMemberStatusChange

                hpicfMvrp.mib
		 -new Trap objects
                      hpicfMvrpVlanLimitReachedEvent

                hpicfRipng.mib
		 -new Trap objects
                      hpicfRipngIfStateChange
                      hpicfRipngIfConfigError
                      hpicfRipngIfRxBadPacket


