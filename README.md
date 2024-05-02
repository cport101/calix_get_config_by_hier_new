# calix_get_config_by_hier
Collect and archive the CALIX AXOS configuration in a hierarchical manner

I find it useful to save the AXOS configure in chunks - facilitates configuration compliance, and is useful in a lab.

<pre>
admin@ub-hmsrv4:~/PY$ python3 ./calix_get_config_by_hier.py
2023-03-15 16:29:36,859 root         INFO     Script is starting
2023-03-15 16:29:36,859 root         INFO     Get target input variables
Enter E9-BNG hostname or E9-BNG address: boron
Enter SSH Username: admin
Enter SSH Password:
Enter SSH Port (if not default 22):
2023-03-15 16:29:49,540 root         INFO     Use login info to ssh and determine AXOS hierarchy
2023-03-15 16:29:51,150 root         INFO     Generate release specific AXOS hierarchy
2023-03-15 16:29:51,153 root         INFO     Building Configuration Directory structure
['boron']
['aaa', 'access-list', 'aggregate-shaper-profile', 'aggregated-service', 'alarm-customization', 'alarm-suppression', 'auto-prov', 'bfd-profile', 'bng', 'bridge', 'call-home', 'card', 'channel-map-profile', 'class-map', 'classless-route-profile', 'cli', 'contact', 'control-plane', 'control-policy', 'cos', 'devices', 'dhcp-v4-relay-profile', 'dhcp-v4-server-pool', 'dhcp-v4-server-profile', 'dhcp-v6-relay-profile', 'dhcp-v6-server-pool', 'dhcp-v6-server-profile', 'dial-plan', 'diameter-client-instance', 'diameter-peer-profile', 'dos-protection-profile', 'dot1x', 'dscp-map', 'dynamic-dba-eir-weight', 'environment-alarm', 'erps-ring', 'est', 'file-transmit-server', 'g8032-ring', 'gnmi', 'gpon-behavior', 'grade-of-service', 'h248-gw-profile', 'host', 'hostname', 'id-profile', 'igmp-profile', 'igmp-ssm-map', 'interface', 'ip', 'ip-unicast-rpf', 'ipv6', 'key', 'l2-dhcp-profile', 'l2-dhcpproxy-profile', 'l2cp-profile', 'l3-dhcp-profile', 'lacp', 'li-client-instance', 'lldp-profile', 'location', 'logging', 'meg', 'mgcp-profile', 'multicast-profile', 'multicast-whitelist-profile', 'mvr-profile', 'netconf', 'nid-ipfix-profile', 'nid-mgmt-profile', 'ntp', 'oam-pm-profile', 'ont', 'ont-power-shedding-timeout-profile', 'ont-profile', 'ont-upgrade', 'ont-upgrade-class', 'ont-upgrade-disable', 'oui-match-list', 'packet-capture', 'policy-actions', 'policy-map', 'pon-cos-profile', 'pon-four-cos-priority-map', 'pon-jitter-delay-profile', 'pon-upstream-policy', 'pppoe-ia-profile', 'pppoe-profile', 'pwe3-profile', 'quarantine', 'quarantine-ont', 'radius-client-instance', 'radius-server-profile', 'rbac', 'remote-mirror', 'reserve-vlan-range', 'rf-avo', 'rg-mgmt-profile', 'router', 'rstp-domain', 'service-oam', 'service-stats-group', 'sip-profile', 'slot', 'snmp', 'ssh', 'streaming', 'subscriber-service-template', 'switchover-on-craft-los', 'system-limits', 'tcpdump', 'tdm-gw-profile', 'techlog-upload', 'timezone', 'transport-service-profile', 'up-down-load', 'upgrade', 'vlan', 'vlan-adaptive-mtu', 'voice-policy-profile', 'voip-profile-server']
2023-03-15 16:29:51,154 root         INFO     Directory tree created
2023-03-15 16:29:52,559 root         INFO     File aaa_cfg.txt was created in file ./boron/aaa/aaa_cfg.txt.
2023-03-15 16:30:04,214 root         INFO     File access-list_cfg.txt was created in file ./boron/access-list/access-list_cfg.txt.
2023-03-15 16:30:15,569 root         INFO     File aggregate-shaper-profile_cfg.txt was created in file ./boron/aggregate-shaper-profile/aggregate-shaper-profile_cfg.txt.
2023-03-15 16:30:26,925 root         INFO     File aggregated-service_cfg.txt was created in file ./boron/aggregated-service/aggregated-service_cfg.txt.
2023-03-15 16:30:38,296 root         INFO     File alarm-customization_cfg.txt was created in file ./boron/alarm-customization/alarm-customization_cfg.txt.
2023-03-15 16:30:49,672 root         INFO     File alarm-suppression_cfg.txt was created in file ./boron/alarm-suppression/alarm-suppression_cfg.txt.
2023-03-15 16:31:01,050 root         INFO     File auto-prov_cfg.txt was created in file ./boron/auto-prov/auto-prov_cfg.txt.
2023-03-15 16:31:12,417 root         INFO     File bfd-profile_cfg.txt was created in file ./boron/bfd-profile/bfd-profile_cfg.txt.
2023-03-15 16:31:23,796 root         INFO     File bng_cfg.txt was created in file ./boron/bng/bng_cfg.txt.
2023-03-15 16:31:35,130 root         INFO     File bridge_cfg.txt was created in file ./boron/bridge/bridge_cfg.txt.
2023-03-15 16:31:46,485 root         INFO     File call-home_cfg.txt was created in file ./boron/call-home/call-home_cfg.txt.
2023-03-15 16:31:57,865 root         INFO     File card_cfg.txt was created in file ./boron/card/card_cfg.txt.
2023-03-15 16:32:09,244 root         INFO     File channel-map-profile_cfg.txt was created in file ./boron/channel-map-profile/channel-map-profile_cfg.txt.
2023-03-15 16:32:21,029 root         INFO     File class-map_cfg.txt was created in file ./boron/class-map/class-map_cfg.txt.
2023-03-15 16:32:32,418 root         INFO     File classless-route-profile_cfg.txt was created in file ./boron/classless-route-profile/classless-route-profile_cfg.txt.
2023-03-15 16:32:43,793 root         INFO     File cli_cfg.txt was created in file ./boron/cli/cli_cfg.txt.
2023-03-15 16:32:55,172 root         INFO     File contact_cfg.txt was created in file ./boron/contact/contact_cfg.txt.
2023-03-15 16:33:06,567 root         INFO     File control-plane_cfg.txt was created in file ./boron/control-plane/control-plane_cfg.txt.
2023-03-15 16:33:18,054 root         INFO     File control-policy_cfg.txt was created in file ./boron/control-policy/control-policy_cfg.txt.
2023-03-15 16:33:29,489 root         INFO     File cos_cfg.txt was created in file ./boron/cos/cos_cfg.txt.
2023-03-15 16:33:40,876 root         INFO     File devices_cfg.txt was created in file ./boron/devices/devices_cfg.txt.
2023-03-15 16:33:52,248 root         INFO     File dhcp-v4-relay-profile_cfg.txt was created in file ./boron/dhcp-v4-relay-profile/dhcp-v4-relay-profile_cfg.txt.
2023-03-15 16:34:03,655 root         INFO     File dhcp-v4-server-pool_cfg.txt was created in file ./boron/dhcp-v4-server-pool/dhcp-v4-server-pool_cfg.txt.
2023-03-15 16:34:15,040 root         INFO     File dhcp-v4-server-profile_cfg.txt was created in file ./boron/dhcp-v4-server-profile/dhcp-v4-server-profile_cfg.txt.
2023-03-15 16:34:26,438 root         INFO     File dhcp-v6-relay-profile_cfg.txt was created in file ./boron/dhcp-v6-relay-profile/dhcp-v6-relay-profile_cfg.txt.
2023-03-15 16:34:37,836 root         INFO     File dhcp-v6-server-pool_cfg.txt was created in file ./boron/dhcp-v6-server-pool/dhcp-v6-server-pool_cfg.txt.
2023-03-15 16:34:49,205 root         INFO     File dhcp-v6-server-profile_cfg.txt was created in file ./boron/dhcp-v6-server-profile/dhcp-v6-server-profile_cfg.txt.
2023-03-15 16:35:00,580 root         INFO     File dial-plan_cfg.txt was created in file ./boron/dial-plan/dial-plan_cfg.txt.
2023-03-15 16:35:11,967 root         INFO     File diameter-client-instance_cfg.txt was created in file ./boron/diameter-client-instance/diameter-client-instance_cfg.txt.
2023-03-15 16:35:23,343 root         INFO     File diameter-peer-profile_cfg.txt was created in file ./boron/diameter-peer-profile/diameter-peer-profile_cfg.txt.
2023-03-15 16:35:34,726 root         INFO     File dos-protection-profile_cfg.txt was created in file ./boron/dos-protection-profile/dos-protection-profile_cfg.txt.
2023-03-15 16:35:46,111 root         INFO     File dot1x_cfg.txt was created in file ./boron/dot1x/dot1x_cfg.txt.
2023-03-15 16:35:57,478 root         INFO     File dscp-map_cfg.txt was created in file ./boron/dscp-map/dscp-map_cfg.txt.
2023-03-15 16:36:08,856 root         INFO     File dynamic-dba-eir-weight_cfg.txt was created in file ./boron/dynamic-dba-eir-weight/dynamic-dba-eir-weight_cfg.txt.
2023-03-15 16:36:20,240 root         INFO     File environment-alarm_cfg.txt was created in file ./boron/environment-alarm/environment-alarm_cfg.txt.
2023-03-15 16:36:31,606 root         INFO     File erps-ring_cfg.txt was created in file ./boron/erps-ring/erps-ring_cfg.txt.
2023-03-15 16:36:42,968 root         INFO     File est_cfg.txt was created in file ./boron/est/est_cfg.txt.
2023-03-15 16:36:54,335 root         INFO     File file-transmit-server_cfg.txt was created in file ./boron/file-transmit-server/file-transmit-server_cfg.txt.
2023-03-15 16:37:05,699 root         INFO     File g8032-ring_cfg.txt was created in file ./boron/g8032-ring/g8032-ring_cfg.txt.
2023-03-15 16:37:17,098 root         INFO     File gnmi_cfg.txt was created in file ./boron/gnmi/gnmi_cfg.txt.
2023-03-15 16:37:28,466 root         INFO     File gpon-behavior_cfg.txt was created in file ./boron/gpon-behavior/gpon-behavior_cfg.txt.
2023-03-15 16:37:39,858 root         INFO     File grade-of-service_cfg.txt was created in file ./boron/grade-of-service/grade-of-service_cfg.txt.
2023-03-15 16:37:51,219 root         INFO     File h248-gw-profile_cfg.txt was created in file ./boron/h248-gw-profile/h248-gw-profile_cfg.txt.
2023-03-15 16:38:02,718 root         INFO     File host_cfg.txt was created in file ./boron/host/host_cfg.txt.
2023-03-15 16:38:14,072 root         INFO     File hostname_cfg.txt was created in file ./boron/hostname/hostname_cfg.txt.
2023-03-15 16:38:25,473 root         INFO     File id-profile_cfg.txt was created in file ./boron/id-profile/id-profile_cfg.txt.
2023-03-15 16:38:36,862 root         INFO     File igmp-profile_cfg.txt was created in file ./boron/igmp-profile/igmp-profile_cfg.txt.
2023-03-15 16:38:48,212 root         INFO     File igmp-ssm-map_cfg.txt was created in file ./boron/igmp-ssm-map/igmp-ssm-map_cfg.txt.
2023-03-15 16:39:05,337 root         INFO     File interface_cfg.txt was created in file ./boron/interface/interface_cfg.txt.
2023-03-15 16:39:17,277 root         INFO     File ip_cfg.txt was created in file ./boron/ip/ip_cfg.txt.
2023-03-15 16:39:28,630 root         INFO     File ip-unicast-rpf_cfg.txt was created in file ./boron/ip-unicast-rpf/ip-unicast-rpf_cfg.txt.
2023-03-15 16:39:40,035 root         INFO     File ipv6_cfg.txt was created in file ./boron/ipv6/ipv6_cfg.txt.
2023-03-15 16:39:51,406 root         INFO     File key_cfg.txt was created in file ./boron/key/key_cfg.txt.
2023-03-15 16:40:02,804 root         INFO     File l2-dhcp-profile_cfg.txt was created in file ./boron/l2-dhcp-profile/l2-dhcp-profile_cfg.txt.
2023-03-15 16:40:14,185 root         INFO     File l2-dhcpproxy-profile_cfg.txt was created in file ./boron/l2-dhcpproxy-profile/l2-dhcpproxy-profile_cfg.txt.
2023-03-15 16:40:25,563 root         INFO     File l2cp-profile_cfg.txt was created in file ./boron/l2cp-profile/l2cp-profile_cfg.txt.
2023-03-15 16:40:36,921 root         INFO     File l3-dhcp-profile_cfg.txt was created in file ./boron/l3-dhcp-profile/l3-dhcp-profile_cfg.txt.
2023-03-15 16:40:48,292 root         INFO     File lacp_cfg.txt was created in file ./boron/lacp/lacp_cfg.txt.
2023-03-15 16:40:59,665 root         INFO     File li-client-instance_cfg.txt was created in file ./boron/li-client-instance/li-client-instance_cfg.txt.
2023-03-15 16:41:11,041 root         INFO     File lldp-profile_cfg.txt was created in file ./boron/lldp-profile/lldp-profile_cfg.txt.
2023-03-15 16:41:22,411 root         INFO     File location_cfg.txt was created in file ./boron/location/location_cfg.txt.
2023-03-15 16:41:33,783 root         INFO     File logging_cfg.txt was created in file ./boron/logging/logging_cfg.txt.
2023-03-15 16:41:45,142 root         INFO     File meg_cfg.txt was created in file ./boron/meg/meg_cfg.txt.
2023-03-15 16:41:56,495 root         INFO     File mgcp-profile_cfg.txt was created in file ./boron/mgcp-profile/mgcp-profile_cfg.txt.
2023-03-15 16:42:07,874 root         INFO     File multicast-profile_cfg.txt was created in file ./boron/multicast-profile/multicast-profile_cfg.txt.
2023-03-15 16:42:19,241 root         INFO     File multicast-whitelist-profile_cfg.txt was created in file ./boron/multicast-whitelist-profile/multicast-whitelist-profile_cfg.txt.
2023-03-15 16:42:30,610 root         INFO     File mvr-profile_cfg.txt was created in file ./boron/mvr-profile/mvr-profile_cfg.txt.
2023-03-15 16:42:41,972 root         INFO     File netconf_cfg.txt was created in file ./boron/netconf/netconf_cfg.txt.
2023-03-15 16:42:53,377 root         INFO     File nid-ipfix-profile_cfg.txt was created in file ./boron/nid-ipfix-profile/nid-ipfix-profile_cfg.txt.
2023-03-15 16:43:04,731 root         INFO     File nid-mgmt-profile_cfg.txt was created in file ./boron/nid-mgmt-profile/nid-mgmt-profile_cfg.txt.
2023-03-15 16:43:16,090 root         INFO     File ntp_cfg.txt was created in file ./boron/ntp/ntp_cfg.txt.
2023-03-15 16:43:27,450 root         INFO     File oam-pm-profile_cfg.txt was created in file ./boron/oam-pm-profile/oam-pm-profile_cfg.txt.
2023-03-15 16:43:38,917 root         INFO     File ont_cfg.txt was created in file ./boron/ont/ont_cfg.txt.
2023-03-15 16:43:50,275 root         INFO     File ont-power-shedding-timeout-profile_cfg.txt was created in file ./boron/ont-power-shedding-timeout-profile/ont-power-shedding-timeout-profile_cfg.txt.
2023-03-15 16:44:02,181 root         INFO     File ont-profile_cfg.txt was created in file ./boron/ont-profile/ont-profile_cfg.txt.
2023-03-15 16:44:13,567 root         INFO     File ont-upgrade_cfg.txt was created in file ./boron/ont-upgrade/ont-upgrade_cfg.txt.
2023-03-15 16:44:24,918 root         INFO     File ont-upgrade-class_cfg.txt was created in file ./boron/ont-upgrade-class/ont-upgrade-class_cfg.txt.
2023-03-15 16:44:36,297 root         INFO     File ont-upgrade-disable_cfg.txt was created in file ./boron/ont-upgrade-disable/ont-upgrade-disable_cfg.txt.
2023-03-15 16:44:47,678 root         INFO     File oui-match-list_cfg.txt was created in file ./boron/oui-match-list/oui-match-list_cfg.txt.
2023-03-15 16:44:59,051 root         INFO     File packet-capture_cfg.txt was created in file ./boron/packet-capture/packet-capture_cfg.txt.
2023-03-15 16:45:11,068 root         INFO     File policy-actions_cfg.txt was created in file ./boron/policy-actions/policy-actions_cfg.txt.
2023-03-15 16:45:33,724 root         INFO     File policy-map_cfg.txt was created in file ./boron/policy-map/policy-map_cfg.txt.
2023-03-15 16:45:45,136 root         INFO     File pon-cos-profile_cfg.txt was created in file ./boron/pon-cos-profile/pon-cos-profile_cfg.txt.
2023-03-15 16:45:56,501 root         INFO     File pon-four-cos-priority-map_cfg.txt was created in file ./boron/pon-four-cos-priority-map/pon-four-cos-priority-map_cfg.txt.
2023-03-15 16:46:07,869 root         INFO     File pon-jitter-delay-profile_cfg.txt was created in file ./boron/pon-jitter-delay-profile/pon-jitter-delay-profile_cfg.txt.
2023-03-15 16:46:19,255 root         INFO     File pon-upstream-policy_cfg.txt was created in file ./boron/pon-upstream-policy/pon-upstream-policy_cfg.txt.
2023-03-15 16:46:30,614 root         INFO     File pppoe-ia-profile_cfg.txt was created in file ./boron/pppoe-ia-profile/pppoe-ia-profile_cfg.txt.
2023-03-15 16:46:41,983 root         INFO     File pppoe-profile_cfg.txt was created in file ./boron/pppoe-profile/pppoe-profile_cfg.txt.
2023-03-15 16:46:53,344 root         INFO     File pwe3-profile_cfg.txt was created in file ./boron/pwe3-profile/pwe3-profile_cfg.txt.
2023-03-15 16:47:04,723 root         INFO     File quarantine_cfg.txt was created in file ./boron/quarantine/quarantine_cfg.txt.
2023-03-15 16:47:16,088 root         INFO     File quarantine-ont_cfg.txt was created in file ./boron/quarantine-ont/quarantine-ont_cfg.txt.
2023-03-15 16:47:27,486 root         INFO     File radius-client-instance_cfg.txt was created in file ./boron/radius-client-instance/radius-client-instance_cfg.txt.
2023-03-15 16:47:38,941 root         INFO     File radius-server-profile_cfg.txt was created in file ./boron/radius-server-profile/radius-server-profile_cfg.txt.
2023-03-15 16:47:50,318 root         INFO     File rbac_cfg.txt was created in file ./boron/rbac/rbac_cfg.txt.
2023-03-15 16:48:01,669 root         INFO     File remote-mirror_cfg.txt was created in file ./boron/remote-mirror/remote-mirror_cfg.txt.
2023-03-15 16:48:13,045 root         INFO     File reserve-vlan-range_cfg.txt was created in file ./boron/reserve-vlan-range/reserve-vlan-range_cfg.txt.
2023-03-15 16:48:24,411 root         INFO     File rf-avo_cfg.txt was created in file ./boron/rf-avo/rf-avo_cfg.txt.
2023-03-15 16:48:35,772 root         INFO     File rg-mgmt-profile_cfg.txt was created in file ./boron/rg-mgmt-profile/rg-mgmt-profile_cfg.txt.
2023-03-15 16:48:47,479 root         INFO     File router_cfg.txt was created in file ./boron/router/router_cfg.txt.
2023-03-15 16:48:58,828 root         INFO     File rstp-domain_cfg.txt was created in file ./boron/rstp-domain/rstp-domain_cfg.txt.
2023-03-15 16:49:10,201 root         INFO     File service-oam_cfg.txt was created in file ./boron/service-oam/service-oam_cfg.txt.
2023-03-15 16:49:21,594 root         INFO     File service-stats-group_cfg.txt was created in file ./boron/service-stats-group/service-stats-group_cfg.txt.
2023-03-15 16:49:32,938 root         INFO     File sip-profile_cfg.txt was created in file ./boron/sip-profile/sip-profile_cfg.txt.
2023-03-15 16:49:44,398 root         INFO     File slot_cfg.txt was created in file ./boron/slot/slot_cfg.txt.
2023-03-15 16:49:55,792 root         INFO     File snmp_cfg.txt was created in file ./boron/snmp/snmp_cfg.txt.
2023-03-15 16:50:07,178 root         INFO     File ssh_cfg.txt was created in file ./boron/ssh/ssh_cfg.txt.
2023-03-15 16:50:18,533 root         INFO     File streaming_cfg.txt was created in file ./boron/streaming/streaming_cfg.txt.
2023-03-15 16:50:29,898 root         INFO     File subscriber-service-template_cfg.txt was created in file ./boron/subscriber-service-template/subscriber-service-template_cfg.txt.
2023-03-15 16:50:41,244 root         INFO     File switchover-on-craft-los_cfg.txt was created in file ./boron/switchover-on-craft-los/switchover-on-craft-los_cfg.txt.
2023-03-15 16:50:52,620 root         INFO     File system-limits_cfg.txt was created in file ./boron/system-limits/system-limits_cfg.txt.
2023-03-15 16:51:03,981 root         INFO     File tcpdump_cfg.txt was created in file ./boron/tcpdump/tcpdump_cfg.txt.
2023-03-15 16:51:15,358 root         INFO     File tdm-gw-profile_cfg.txt was created in file ./boron/tdm-gw-profile/tdm-gw-profile_cfg.txt.
2023-03-15 16:51:26,749 root         INFO     File techlog-upload_cfg.txt was created in file ./boron/techlog-upload/techlog-upload_cfg.txt.
2023-03-15 16:51:38,126 root         INFO     File timezone_cfg.txt was created in file ./boron/timezone/timezone_cfg.txt.
2023-03-15 16:51:49,492 root         INFO     File transport-service-profile_cfg.txt was created in file ./boron/transport-service-profile/transport-service-profile_cfg.txt.
2023-03-15 16:52:00,899 root         INFO     File up-down-load_cfg.txt was created in file ./boron/up-down-load/up-down-load_cfg.txt.
2023-03-15 16:52:12,270 root         INFO     File upgrade_cfg.txt was created in file ./boron/upgrade/upgrade_cfg.txt.
2023-03-15 16:52:23,859 root         INFO     File vlan_cfg.txt was created in file ./boron/vlan/vlan_cfg.txt.
2023-03-15 16:52:35,221 root         INFO     File vlan-adaptive-mtu_cfg.txt was created in file ./boron/vlan-adaptive-mtu/vlan-adaptive-mtu_cfg.txt.
2023-03-15 16:52:46,607 root         INFO     File voice-policy-profile_cfg.txt was created in file ./boron/voice-policy-profile/voice-policy-profile_cfg.txt.
2023-03-15 16:52:57,965 root         INFO     File voip-profile-server_cfg.txt was created in file ./boron/voip-profile-server/voip-profile-server_cfg.txt.
ttt@ub-hmsrv4:~/PY$ 

121 directories, 68 files
admin@ub-hmsrv4:~/PY$ tree ./boron/
./boron/
├── aaa
│   └── aaa_cfg.txt
├── access-list
│   └── access-list_cfg.txt
├── aggregated-service
│   └── aggregated-service_cfg.txt
├── aggregate-shaper-profile
│   └── aggregate-shaper-profile_cfg.txt
├── alarm-customization
│   └── alarm-customization_cfg.txt
├── alarm-suppression
│   └── alarm-suppression_cfg.txt
├── auto-prov
│   └── auto-prov_cfg.txt
├── bfd-profile
│   └── bfd-profile_cfg.txt
├── bng
│   └── bng_cfg.txt
├── bridge
│   └── bridge_cfg.txt
├── call-home
│   └── call-home_cfg.txt
├── card
│   └── card_cfg.txt
├── channel-map-profile
│   └── channel-map-profile_cfg.txt
├── classless-route-profile
│   └── classless-route-profile_cfg.txt
├── class-map
│   └── class-map_cfg.txt
├── cli
│   └── cli_cfg.txt
├── contact
│   └── contact_cfg.txt
├── control-plane
│   └── control-plane_cfg.txt
├── control-policy
│   └── control-policy_cfg.txt
├── cos
│   └── cos_cfg.txt
├── devices
│   └── devices_cfg.txt
├── dhcp-v4-relay-profile
│   └── dhcp-v4-relay-profile_cfg.txt
├── dhcp-v4-server-pool
│   └── dhcp-v4-server-pool_cfg.txt
├── dhcp-v4-server-profile
│   └── dhcp-v4-server-profile_cfg.txt
├── dhcp-v6-relay-profile
│   └── dhcp-v6-relay-profile_cfg.txt
├── dhcp-v6-server-pool
│   └── dhcp-v6-server-pool_cfg.txt
├── dhcp-v6-server-profile
│   └── dhcp-v6-server-profile_cfg.txt
├── dial-plan
│   └── dial-plan_cfg.txt
├── diameter-client-instance
│   └── diameter-client-instance_cfg.txt
├── diameter-peer-profile
│   └── diameter-peer-profile_cfg.txt
├── dos-protection-profile
│   └── dos-protection-profile_cfg.txt
├── dot1x
│   └── dot1x_cfg.txt
├── dscp-map
│   └── dscp-map_cfg.txt
├── dynamic-dba-eir-weight
│   └── dynamic-dba-eir-weight_cfg.txt
├── environment-alarm
│   └── environment-alarm_cfg.txt
├── erps-ring
│   └── erps-ring_cfg.txt
├── est
│   └── est_cfg.txt
├── file-transmit-server
│   └── file-transmit-server_cfg.txt
├── g8032-ring
│   └── g8032-ring_cfg.txt
├── gnmi
│   └── gnmi_cfg.txt
├── gpon-behavior
│   └── gpon-behavior_cfg.txt
├── grade-of-service
│   └── grade-of-service_cfg.txt
├── h248-gw-profile
│   └── h248-gw-profile_cfg.txt
├── host
│   └── host_cfg.txt
├── hostname
│   └── hostname_cfg.txt
├── id-profile
│   └── id-profile_cfg.txt
├── igmp-profile
│   └── igmp-profile_cfg.txt
├── igmp-ssm-map
│   └── igmp-ssm-map_cfg.txt
├── interface
│   └── interface_cfg.txt
├── ip
│   └── ip_cfg.txt
├── ip-unicast-rpf
│   └── ip-unicast-rpf_cfg.txt
├── ipv6
│   └── ipv6_cfg.txt
├── key
│   └── key_cfg.txt
├── l2cp-profile
│   └── l2cp-profile_cfg.txt
├── l2-dhcp-profile
│   └── l2-dhcp-profile_cfg.txt
├── l2-dhcpproxy-profile
│   └── l2-dhcpproxy-profile_cfg.txt
├── l3-dhcp-profile
│   └── l3-dhcp-profile_cfg.txt
├── lacp
│   └── lacp_cfg.txt
├── li-client-instance
│   └── li-client-instance_cfg.txt
├── lldp-profile
│   └── lldp-profile_cfg.txt
├── location
│   └── location_cfg.txt
├── logging
│   └── logging_cfg.txt
├── meg
│   └── meg_cfg.txt
├── mgcp-profile
│   └── mgcp-profile_cfg.txt
├── multicast-profile
│   └── multicast-profile_cfg.txt
├── multicast-whitelist-profile
│   └── multicast-whitelist-profile_cfg.txt
├── mvr-profile
│   └── mvr-profile_cfg.txt
├── netconf
│   └── netconf_cfg.txt
├── nid-ipfix-profile
│   └── nid-ipfix-profile_cfg.txt
├── nid-mgmt-profile
│   └── nid-mgmt-profile_cfg.txt
├── ntp
│   └── ntp_cfg.txt
├── oam-pm-profile
│   └── oam-pm-profile_cfg.txt
├── ont
│   └── ont_cfg.txt
├── ont-power-shedding-timeout-profile
│   └── ont-power-shedding-timeout-profile_cfg.txt
├── ont-profile
│   └── ont-profile_cfg.txt
├── ont-upgrade
│   └── ont-upgrade_cfg.txt
├── ont-upgrade-class
│   └── ont-upgrade-class_cfg.txt
├── ont-upgrade-disable
│   └── ont-upgrade-disable_cfg.txt
├── oui-match-list
│   └── oui-match-list_cfg.txt
├── packet-capture
│   └── packet-capture_cfg.txt
├── policy-actions
│   └── policy-actions_cfg.txt
├── policy-map
│   └── policy-map_cfg.txt
├── pon-cos-profile
│   └── pon-cos-profile_cfg.txt
├── pon-four-cos-priority-map
│   └── pon-four-cos-priority-map_cfg.txt
├── pon-jitter-delay-profile
│   └── pon-jitter-delay-profile_cfg.txt
├── pon-upstream-policy
│   └── pon-upstream-policy_cfg.txt
├── pppoe-ia-profile
│   └── pppoe-ia-profile_cfg.txt
├── pppoe-profile
│   └── pppoe-profile_cfg.txt
├── pwe3-profile
│   └── pwe3-profile_cfg.txt
├── quarantine
│   └── quarantine_cfg.txt
├── quarantine-ont
│   └── quarantine-ont_cfg.txt
├── radius-client-instance
│   └── radius-client-instance_cfg.txt
├── radius-server-profile
│   └── radius-server-profile_cfg.txt
├── rbac
│   └── rbac_cfg.txt
├── remote-mirror
│   └── remote-mirror_cfg.txt
├── reserve-vlan-range
│   └── reserve-vlan-range_cfg.txt
├── rf-avo
│   └── rf-avo_cfg.txt
├── rg-mgmt-profile
│   └── rg-mgmt-profile_cfg.txt
├── router
│   └── router_cfg.txt
├── rstp-domain
│   └── rstp-domain_cfg.txt
├── service-oam
│   └── service-oam_cfg.txt
├── service-stats-group
│   └── service-stats-group_cfg.txt
├── sip-profile
│   └── sip-profile_cfg.txt
├── slot
│   └── slot_cfg.txt
├── snmp
│   └── snmp_cfg.txt
├── ssh
│   └── ssh_cfg.txt
├── streaming
│   └── streaming_cfg.txt
├── subscriber-service-template
│   └── subscriber-service-template_cfg.txt
├── switchover-on-craft-los
│   └── switchover-on-craft-los_cfg.txt
├── system-limits
│   └── system-limits_cfg.txt
├── tcpdump
│   └── tcpdump_cfg.txt
├── tdm-gw-profile
│   └── tdm-gw-profile_cfg.txt
├── techlog-upload
│   └── techlog-upload_cfg.txt
├── timezone
│   └── timezone_cfg.txt
├── transport-service-profile
│   └── transport-service-profile_cfg.txt
├── up-down-load
│   └── up-down-load_cfg.txt
├── upgrade
│   └── upgrade_cfg.txt
├── vlan
│   └── vlan_cfg.txt
├── vlan-adaptive-mtu
│   └── vlan-adaptive-mtu_cfg.txt
├── voice-policy-profile
│   └── voice-policy-profile_cfg.txt
└── voip-profile-server
    └── voip-profile-server_cfg.txt

121 directories, 121 files
admin@ub-hmsrv4:~/PY$ 
</pre>
