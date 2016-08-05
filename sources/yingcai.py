# encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

industry_list = {
	"1001": {
		"1001": {
			"1001": {
				"cn": " 高级硬件工程师 ",
				"en": " Senior Hardware Engineer "
			},
			"1002": {
				"cn": " 硬件工程师 ",
				"en": " Hardware Engineer "
			},
			"1003": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1002": {
			"1004": {
				"cn": " 高级软件工程师 ",
				"en": " Senior Software Engineer "
			},
			"1005": {
				"cn": " 软件工程师 ",
				"en": " Software Engineer "
			},
			"1006": {
				"cn": " 软件UI设计师/工程师 ",
				"en": " Software UI/ Designer Engineer "
			},
			"1007": {
				"cn": " 仿真应用工程师 ",
				"en": " Simulation Application Engineer "
			},
			"1008": {
				"cn": " ERP实施顾问 ",
				"en": " ERP Implementation "
			},
			"1009": {
				"cn": " ERP技术开发 ",
				"en": " ERP R&D "
			},
			"1010": {
				"cn": " 需求工程师 ",
				"en": " Demand / Specification Engineer "
			},
			"1011": {
				"cn": " 系统集成工程师 ",
				"en": " System Integration Engineer "
			},
			"1012": {
				"cn": " 系统分析员 ",
				"en": " System Analyst "
			},
			"1013": {
				"cn": " 系统工程师 ",
				"en": " System Engineer "
			},
			"1014": {
				"cn": " 系统架构设计师 ",
				"en": " System Architecture Design "
			},
			"1015": {
				"cn": " 数据库工程师/管理员 ",
				"en": " Database Engineer/Administrator "
			},
			"1016": {
				"cn": " 计算机辅助设计工程师 ",
				"en": " Computer Aided Design Engineer "
			},
			"1017": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1003": {
			"1018": {
				"cn": " 互联网软件开发工程师 ",
				"en": " Internet/E-Commerce Software Engineer "
			},
			"1019": {
				"cn": " 多媒体/游戏开发工程师 ",
				"en": " Multimedia/Game Development Engineer "
			},
			"1020": {
				"cn": " 网站营运经理/主管 ",
				"en": " Web Operations Manager/Supervisor "
			},
			"1021": {
				"cn": " 网络工程师 ",
				"en": " Network Engineer "
			},
			"1022": {
				"cn": " 系统管理员/网络管理员 ",
				"en": " System Manager/Webmaster "
			},
			"1023": {
				"cn": " 网站策划 ",
				"en": " Web Producer "
			},
			"1024": {
				"cn": " 网站编辑 ",
				"en": " Web Editor "
			},
			"1025": {
				"cn": " 网页设计/制作/美工 ",
				"en": " Web Designer/Production/Creative "
			},
			"1026": {
				"cn": " 网络信息安全工程师 ",
				"en": " Information Security Engineer "
			},
			"1027": {
				"cn": " 网站架构设计师 ",
				"en": " Web Architecture Design "
			},
			"1028": {
				"cn": " 网站维护工程师 ",
				"en": " Web Maintenance Engineer "
			},
			"1029": {
				"cn": " 语音/视频开发工程师 ",
				"en": " Audio/Video Development Engineer "
			},
			"1030": {
				"cn": " UI设计师/顾问 ",
				"en": " UI Designer / Consultant "
			},
			"1031": {
				"cn": " 网站营运专员 ",
				"en": " Web Operations Specialist "
			},
			"1032": {
				"cn": " 脚本开发工程师 ",
				"en": " Script Development Engineer "
			},
			"1033": {
				"cn": " 游戏策划师 ",
				"en": " Game Planner "
			},
			"1034": {
				"cn": " 游戏界面设计师 ",
				"en": " Game UI Designer "
			},
			"1035": {
				"cn": " Flash设计/开发 ",
				"en": " Flash Designer/Developer "
			},
			"1036": {
				"cn": " 特效设计师 ",
				"en": " Special Effects Designer "
			},
			"1037": {
				"cn": " 视觉设计师 ",
				"en": " Visual Effects Designer "
			},
			"1038": {
				"cn": " 音效设计师 ",
				"en": " Sound Effects Designer "
			},
			"1039": {
				"cn": " SEO搜索引擎优化 ",
				"en": " SEO Specialist "
			},
			"1040": {
				"cn": " 产品经理/主管 ",
				"en": " Product Manager/Supervisor "
			},
			"1041": {
				"cn": " 产品专员 ",
				"en": " Product Specialist "
			},
			"1042": {
				"cn": " 电子商务经理/主管 ",
				"en": " E-Commerce Manager/Supervisor "
			},
			"1043": {
				"cn": " 电子商务专员 ",
				"en": " E-Commerce Specialist "
			},
			"1044": {
				"cn": " 网店店长/客服 ",
				"en": " Online Shop Manager/Customer Service "
			},
			"1045": {
				"cn": " 网站营运总监 ",
				"en": " Web Operations Director "
			},
			"1046": {
				"cn": " 产品总监 ",
				"en": " Product Director "
			},
			"1047": {
				"cn": " 网络推广总监 ",
				"en": " Online Marketing Director "
			},
			"1048": {
				"cn": " 网络推广经理/主管 ",
				"en": " Online Marketing Manager/Supervisor "
			},
			"1049": {
				"cn": " 网络推广专员 ",
				"en": " Online Marketing Specialist "
			},
			"1050": {
				"cn": " 电子商务总监 ",
				"en": " E-Commerce Director "
			},
			"1051": {
				"cn": " 交互设计师 ",
				"en": " Interaction Designer "
			},
			"1052": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1004": {
			"1053": {
				"cn": " 首席技术执行官CTO/首席信息官CIO ",
				"en": " Chief Technology Officer CTO/Chief Information Officer CIO "
			},
			"1054": {
				"cn": " 技术总监/经理 ",
				"en": " Technical Director/Manager "
			},
			"1055": {
				"cn": " 信息技术经理/主管 ",
				"en": " IT Manager/Supervisor "
			},
			"1056": {
				"cn": " 信息技术专员 ",
				"en": " IT Specialist "
			},
			"1057": {
				"cn": " 项目总监 ",
				"en": " Project Director "
			},
			"1058": {
				"cn": " 项目经理 ",
				"en": " Project Manager "
			},
			"1059": {
				"cn": " 项目主管 ",
				"en": " Project Supervisor "
			},
			"1060": {
				"cn": " 项目执行/协调人员 ",
				"en": " Project Specialist / Coordinator "
			},
			"1061": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1005": {
			"1062": {
				"cn": " 技术支持/维护经理 ",
				"en": " Technical Support/Maintenance Manager "
			},
			"1063": {
				"cn": " 技术支持/维护工程师 ",
				"en": " Technical Support/Maintenance Engineer "
			},
			"1064": {
				"cn": " 计量工程师 ",
				"en": " Measure Engineer "
			},
			"1065": {
				"cn": " 标准化工程师 ",
				"en": " Standardization Engineer "
			},
			"1066": {
				"cn": " 品质经理 ",
				"en": " Quality Assurance QA Manager "
			},
			"1067": {
				"cn": " 系统测试 ",
				"en": " Systems Testing QA "
			},
			"1068": {
				"cn": " 软件测试 ",
				"en": " Software Testing QA "
			},
			"1069": {
				"cn": " 硬件测试 ",
				"en": " Hardware Testing QA "
			},
			"1070": {
				"cn": " 测试员 ",
				"en": " Test Engineer /Tester "
			},
			"1071": {
				"cn": " 技术文员/助理 ",
				"en": " Technical Clerk/Assistant "
			},
			"1072": {
				"cn": " Helpdesk 技术支持 ",
				"en": " Helpdesk "
			},
			"1073": {
				"cn": " 文档工程师 ",
				"en": " Technical Writer "
			},
			"1074": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1006": {
			"1075": {
				"cn": " 通信技术工程师 ",
				"en": " Communication Engineer "
			},
			"1076": {
				"cn": " 有线传输工程师 ",
				"en": " Wired Transmission Engineer "
			},
			"1077": {
				"cn": " 无线通信工程师 ",
				"en": " Wireless Communication Engineer "
			},
			"1078": {
				"cn": " 电信交换工程师 ",
				"en": " Telecommunication Exchange Engineer "
			},
			"1079": {
				"cn": " 数据通信工程师 ",
				"en": " Data Communication Engineer "
			},
			"1080": {
				"cn": " 移动通信工程师 ",
				"en": " Mobile Communication Engineer "
			},
			"1081": {
				"cn": " 电信网络工程师 ",
				"en": " Telecommunication Network Engineer "
			},
			"1082": {
				"cn": " 通信电源工程师 ",
				"en": " Communication Power Supply Engineer "
			},
			"1083": {
				"cn": " 增值产品开发工程师 ",
				"en": " Value-Added Product Development Engineer "
			},
			"1084": {
				"cn": " 手机软件开发工程师 ",
				"en": " Mobile Software Development Engineer "
			},
			"1085": {
				"cn": " 手机应用开发工程师 ",
				"en": " Mobile Application Development Engineer "
			},
			"1086": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1007": {
			"1087": {
				"cn": " 集成电路IC设计/应用工程师 ",
				"en": " IC Design/Application Engineer "
			},
			"1088": {
				"cn": " IC验证工程师 ",
				"en": " IC Verification Engineer "
			},
			"1089": {
				"cn": " 电子工程师/技术员 ",
				"en": " Electronics Engineer "
			},
			"1090": {
				"cn": " 电气工程师/技术员 ",
				"en": " Electrical Engineer "
			},
			"1091": {
				"cn": " 电路工程师/技术员(模拟/数字) ",
				"en": " Electronic Circuit Engineer(Analog/Digital) "
			},
			"1092": {
				"cn": " 电声/音响工程师/技术员 ",
				"en": " Electroacoustics Engineer "
			},
			"1093": {
				"cn": " 半导体技术 ",
				"en": " Semiconductor Technology "
			},
			"1094": {
				"cn": " 自动控制工程师/技术员 ",
				"en": " Autocontrol Engineer/Technician "
			},
			"1095": {
				"cn": " 电子软件开发(ARM/MCU...) ",
				"en": " Electronics Software (ARM/MCU…) "
			},
			"1096": {
				"cn": " 嵌入式软件开发(Linux/单片机/DLC/DSP…) ",
				"en": " Embedded Software Engineer (Linux/SCM/DLC/DSP…) "
			},
			"1097": {
				"cn": " 电池/电源开发 ",
				"en": " Battery/Power Engineer "
			},
			"1098": {
				"cn": " FAE 现场应用工程师 ",
				"en": " Field Application Engineer (FAE) "
			},
			"1099": {
				"cn": " 家用电器/数码产品研发 ",
				"en": " Household Electronics/Digital Products Development "
			},
			"1100": {
				"cn": " 仪器/仪表/计量分析师 ",
				"en": " Instrument/Measurement Analyst "
			},
			"1101": {
				"cn": " 测试工程师 ",
				"en": " Quality Testing Engineer "
			},
			"1102": {
				"cn": " 电子技术研发工程师 ",
				"en": " Electronics Development Engineer "
			},
			"1103": {
				"cn": " 激光/光电子技术 ",
				"en": " Laser/Optoelectronics Technology "
			},
			"1104": {
				"cn": " 嵌入式硬件开发(主板机…) ",
				"en": " Embedded Hardware Engineer(PCB…) "
			},
			"1105": {
				"cn": " 电子/电器维修工程师/技师 ",
				"en": " Electronic/Electrical Appliance Technologist "
			},
			"1106": {
				"cn": " 变压器与磁电工程师 ",
				"en": " Transformer and Magnetoelectricity Engineer "
			},
			"1107": {
				"cn": " 版图设计工程师 ",
				"en": " Layout Design Engineer "
			},
			"1108": {
				"cn": " 工艺工程师 ",
				"en": " Process Engineer "
			},
			"1109": {
				"cn": " 射频工程师 ",
				"en": " RF Engineer "
			},
			"1110": {
				"cn": " 其他 ",
				"en": " Others "
			}
		}
	},
	"1002": {
		"1008": {
			"1111": {
				"cn": " 销售总监 ",
				"en": " Sales Director "
			},
			"1112": {
				"cn": " 销售经理 ",
				"en": " Sales Manager "
			},
			"1113": {
				"cn": " 销售主管 ",
				"en": " Sales Supervisor "
			},
			"1114": {
				"cn": " 业务拓展主管/经理 ",
				"en": " Business Development Supervisor/Manager "
			},
			"1115": {
				"cn": " 渠道/分销总监 ",
				"en": " Channel/Distribution Director "
			},
			"1116": {
				"cn": " 渠道/分销经理 ",
				"en": " Channel/Distribution Manager "
			},
			"1117": {
				"cn": " 渠道/分销主管 ",
				"en": " Channel/Distribution Supervisor "
			},
			"1118": {
				"cn": " 大客户销售管理 ",
				"en": " Key Account Sales Management "
			},
			"1119": {
				"cn": " 客户经理/主管 ",
				"en": " Sales Account Manager/Supervisor "
			},
			"1120": {
				"cn": " 区域销售总监 ",
				"en": " Regional Sales Director "
			},
			"1121": {
				"cn": " 区域销售经理 ",
				"en": " Regional Sales Manager "
			},
			"1122": {
				"cn": " 团购经理/主管 ",
				"en": " Group Purchase Manager/Supervisor "
			},
			"1123": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1009": {
			"1124": {
				"cn": " 销售代表 ",
				"en": " Sales Representative / Executive "
			},
			"1125": {
				"cn": " 渠道/分销专员 ",
				"en": " Channel/Distribution Representative "
			},
			"1126": {
				"cn": " 客户代表 ",
				"en": " Sales Account Representative "
			},
			"1127": {
				"cn": " 销售工程师 ",
				"en": " Sales Engineer "
			},
			"1128": {
				"cn": " 电话销售 ",
				"en": " Telesales "
			},
			"1129": {
				"cn": " 经销商 ",
				"en": " Distributor "
			},
			"1130": {
				"cn": " 团购业务员 ",
				"en": " Group Purchase Representative "
			},
			"1131": {
				"cn": " 大客户销售 ",
				"en": " Key Account Sales "
			},
			"1132": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1010": {
			"1133": {
				"cn": " 销售行政经理/主管 ",
				"en": " Sales Admin. Manager/Supervisor "
			},
			"1134": {
				"cn": " 销售行政专员/助理 ",
				"en": " Sales Admin. Executive/Assistant "
			},
			"1135": {
				"cn": " 商务经理 ",
				"en": " Business Manager "
			},
			"1136": {
				"cn": " 商务主管/专员 ",
				"en": " Business Supervisor/Executive "
			},
			"1137": {
				"cn": " 商务助理 ",
				"en": " Business Assistant "
			},
			"1138": {
				"cn": " 销售助理 ",
				"en": " Sales Assistant / Trainee "
			},
			"1139": {
				"cn": " 业务分析经理/主管 ",
				"en": " Business Analysis Manager/Supervisor "
			},
			"1140": {
				"cn": " 业务分析专员/助理 ",
				"en": " Business Analysis Specialist/Assistant "
			},
			"1141": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1011": {
			"1142": {
				"cn": " 客服总监(非技术) ",
				"en": " Customer Service Director "
			},
			"1143": {
				"cn": " 客服经理(非技术) ",
				"en": " Customer Service Manager "
			},
			"1144": {
				"cn": " 客服主管(非技术) ",
				"en": " Customer Service Supervisor "
			},
			"1145": {
				"cn": " 客服专员/助理(非技术) ",
				"en": " Customer Service Executive/Assistant "
			},
			"1146": {
				"cn": " 售前/售后技术支持经理 ",
				"en": " Technical Support Manager "
			},
			"1147": {
				"cn": " 售前/售后技术支持主管 ",
				"en": " Technical Support Supervisor "
			},
			"1148": {
				"cn": " 售前/售后技术支持工程师 ",
				"en": " Technical Support Engineer "
			},
			"1149": {
				"cn": " 咨询热线/呼叫中心服务人员 ",
				"en": " Customer Hot Line/Call Center Staff "
			},
			"1150": {
				"cn": " 客户关系经理/主管 ",
				"en": " Customer Relations Management "
			},
			"1151": {
				"cn": " 投诉专员 ",
				"en": " Complaints Specialist "
			},
			"1152": {
				"cn": " VIP专员 ",
				"en": " VIP Member Specialist "
			},
			"1153": {
				"cn": " 其他 ",
				"en": " Others "
			}
		}
	},
	"1003": {
		"1012": {
			"1154": {
				"cn": " 首席财务官 CFO ",
				"en": " Chief Financial Officer CFO "
			},
			"1155": {
				"cn": " 财务总监 ",
				"en": " Finance Controller / Director "
			},
			"1156": {
				"cn": " 财务经理 ",
				"en": " Finance Manager "
			},
			"1157": {
				"cn": " 财务顾问 ",
				"en": " Finance Consultant "
			},
			"1158": {
				"cn": " 财务主管/总帐主管 ",
				"en": " Finance Supervisor "
			},
			"1159": {
				"cn": " 会计经理/会计主管 ",
				"en": " Accounting Manager/Supervisor "
			},
			"1160": {
				"cn": " 会计 ",
				"en": " Accountant / Accounting Trainee "
			},
			"1161": {
				"cn": " 出纳员 ",
				"en": " Cashier "
			},
			"1162": {
				"cn": " 财务/会计助理 ",
				"en": " Finance/Accounting Assistant "
			},
			"1163": {
				"cn": " 会计文员 ",
				"en": " Accounting Clerk "
			},
			"1164": {
				"cn": " 固定资产会计 ",
				"en": " Fixed Asset Accounting "
			},
			"1165": {
				"cn": " 财务分析经理/主管 ",
				"en": " Financial Analysis Manager/Supervisor "
			},
			"1166": {
				"cn": " 财务分析员 ",
				"en": " Financial Analyst "
			},
			"1167": {
				"cn": " 成本经理/成本主管 ",
				"en": " Cost Accounting Manager/Supervisor "
			},
			"1168": {
				"cn": " 成本管理员 ",
				"en": " Cost Accounting Specialist "
			},
			"1169": {
				"cn": " 资金经理/主管 ",
				"en": " Treasury Manager/Supervisor "
			},
			"1170": {
				"cn": " 资金专员 ",
				"en": " Treasury Specialist "
			},
			"1171": {
				"cn": " 审计经理/主管 ",
				"en": " Audit Manager/Supervisor "
			},
			"1172": {
				"cn": " 审计专员/助理 ",
				"en": " Audit Executive/Assistant "
			},
			"1173": {
				"cn": " 税务经理/税务主管 ",
				"en": " Tax Manager/Supervisor "
			},
			"1174": {
				"cn": " 税务专员/助理 ",
				"en": " Tax Executive/Assistant "
			},
			"1175": {
				"cn": " 统计员 ",
				"en": " Statistician "
			},
			"1176": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1013": {
			"1177": {
				"cn": " 证券/期货/外汇经纪人 ",
				"en": " Securities Broker "
			},
			"1178": {
				"cn": " 证券分析师 ",
				"en": " Securities Analyst "
			},
			"1179": {
				"cn": " 股票/期货操盘手 ",
				"en": " Stocks/Futures Operator "
			},
			"1180": {
				"cn": " 金融/经济研究员 ",
				"en": " Financial Analyst/Economist "
			},
			"1181": {
				"cn": " 投资/基金项目经理 ",
				"en": " Investment Manager/Fund Manager "
			},
			"1182": {
				"cn": " 投资/理财顾问 ",
				"en": " Investment/Financial Management Advisor "
			},
			"1183": {
				"cn": " 投资银行业务 ",
				"en": " Investment Banking Specialist "
			},
			"1184": {
				"cn": " 融资经理/融资主管 ",
				"en": " Treasury Manager/Supervisor "
			},
			"1185": {
				"cn": " 融资专员 ",
				"en": " Treasury Specialist "
			},
			"1186": {
				"cn": " 拍卖/担保/典当业务 ",
				"en": " Auction/Guarantee/Pawn Business "
			},
			"1187": {
				"cn": " 金融产品经理 ",
				"en": " Financial Product Manager "
			},
			"1188": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1014": {
			"1189": {
				"cn": " 行长/副行长 ",
				"en": " President/Vice-President/Branch Manager "
			},
			"1190": {
				"cn": " 资产评估/分析 ",
				"en": " Assets Valuation/Analyst "
			},
			"1191": {
				"cn": " 风险控制 ",
				"en": " Risk Management "
			},
			"1192": {
				"cn": " 进出口/信用证结算 ",
				"en": " Trading / LC Officer "
			},
			"1193": {
				"cn": " 清算人员 ",
				"en": " Settlement Officer "
			},
			"1194": {
				"cn": " 外汇交易 ",
				"en": " Foreign Exchange "
			},
			"1195": {
				"cn": " 高级客户经理/客户经理 ",
				"en": " Senior Relationship Manager "
			},
			"1196": {
				"cn": " 客户主管/专员 ",
				"en": " Relationship Supervisor/Executive "
			},
			"1197": {
				"cn": " 信贷管理 ",
				"en": " Loan/Credit Officer "
			},
			"1198": {
				"cn": " 银行柜员 ",
				"en": " Bank Teller "
			},
			"1199": {
				"cn": " 银行卡、电子银行业务推广 ",
				"en": " Credit Card/E-banking business Develop "
			},
			"1200": {
				"cn": " 个人业务部门经理/主管 ",
				"en": " Personal Banking Manager/Supervisor "
			},
			"1201": {
				"cn": " 个人业务客户经理 ",
				"en": " Personal Banking Account Manager "
			},
			"1202": {
				"cn": " 公司业务部门经理/主管 ",
				"en": " Corporate Banking Manager "
			},
			"1203": {
				"cn": " 公司业务客户经理 ",
				"en": " Corporate Banking Account Manager "
			},
			"1204": {
				"cn": " 综合业务经理/主管 ",
				"en": " Integrated Service Manager/Supervisor "
			},
			"1205": {
				"cn": " 综合业务专员 ",
				"en": " Integrated Service Officer "
			},
			"1206": {
				"cn": " 信审核查 ",
				"en": " Credit Review "
			},
			"1207": {
				"cn": " 营业部大堂经理 ",
				"en": " Branch Lobby Manager "
			},
			"1208": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1015": {
			"1209": {
				"cn": " 保险精算师 ",
				"en": " Actuary "
			},
			"1210": {
				"cn": " 保险产品开发/项目策划 ",
				"en": " Product Development/Planner "
			},
			"1211": {
				"cn": " 保险业务经理/主管 ",
				"en": " Business Manager/Supervisor "
			},
			"1212": {
				"cn": " 保险代理/经纪人/客户经理 ",
				"en": " Agent/Broker/Account Manager "
			},
			"1213": {
				"cn": " 理财顾问/财务规划师 ",
				"en": " Financial Advisor/Financial Planner "
			},
			"1214": {
				"cn": " 储备经理人 ",
				"en": " Agency Management Associate "
			},
			"1215": {
				"cn": " 保险核保 ",
				"en": " Underwriting "
			},
			"1216": {
				"cn": " 保险理赔 ",
				"en": " Claim Management "
			},
			"1217": {
				"cn": " 保险客户服务/续期管理 ",
				"en": " Customer Service "
			},
			"1218": {
				"cn": " 保险培训师 ",
				"en": " Trainer "
			},
			"1219": {
				"cn": " 保险内勤 ",
				"en": " Staff "
			},
			"1220": {
				"cn": " 契约管理 ",
				"en": " Policy Management "
			},
			"1221": {
				"cn": " 其他 ",
				"en": " Others "
			}
		}
	},
	"1004": {
		"1016": {
			"1222": {
				"cn": " 工厂经理/厂长 ",
				"en": " Plant/Factory Manager "
			},
			"1223": {
				"cn": " 总工程师/副总工程师 ",
				"en": " Chief Engineer "
			},
			"1224": {
				"cn": " 项目经理/主管 ",
				"en": " Project Manager/Supervisor "
			},
			"1225": {
				"cn": " 项目工程师 ",
				"en": " Project Engineer "
			},
			"1226": {
				"cn": " 营运经理 ",
				"en": " Operations Manager "
			},
			"1227": {
				"cn": " 营运主管 ",
				"en": " Operations Supervisor "
			},
			"1228": {
				"cn": " 生产经理/车间主任 ",
				"en": " Production Manager/Workshop Supervisor "
			},
			"1229": {
				"cn": " 生产计划/物料管理(PMC) ",
				"en": " Planner/PMC "
			},
			"1230": {
				"cn": " 生产主管/督导/领班/组长 ",
				"en": " Production Supervisor/Team Leader "
			},
			"1231": {
				"cn": " 化验员 ",
				"en": " Laboratory Technician "
			},
			"1232": {
				"cn": " 生产文员 ",
				"en": " Clerk "
			},
			"1233": {
				"cn": " 项目总监 ",
				"en": " Project Director "
			},
			"1234": {
				"cn": " 生产总监 ",
				"en": " Production Director "
			},
			"1235": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1017": {
			"1236": {
				"cn": " 质量管理/测试经理(QA/QC经理) ",
				"en": " QA/QC Manager "
			},
			"1237": {
				"cn": " 质量管理/测试主管(QA/QC主管) ",
				"en": " QA/QC Supervisor "
			},
			"1238": {
				"cn": " 质量管理/测试工程师(QA/QC工程师) ",
				"en": " QA/QC Engineer "
			},
			"1239": {
				"cn": " 质量检验员/测试员 ",
				"en": " Quality Inspector/Tester "
			},
			"1240": {
				"cn": " 可靠度工程师 ",
				"en": " Reliability Engineer "
			},
			"1241": {
				"cn": " 故障分析工程师 ",
				"en": " Failure Analysis Engineer "
			},
			"1242": {
				"cn": " 认证工程师/审核员 ",
				"en": " Certification Engineer/Auditor "
			},
			"1243": {
				"cn": " 体系工程师/审核员 ",
				"en": " Systems Engineer/Auditor "
			},
			"1244": {
				"cn": " 环境/健康/安全经理/主管（EHS） ",
				"en": " Environmental/Health/ Safety Manager/Supervisor "
			},
			"1245": {
				"cn": " 环境/健康/安全工程师（EHS） ",
				"en": " Environmental/Health/ Safety Engineer "
			},
			"1246": {
				"cn": " 供应商管理 ",
				"en": " Supplier/Vendor Management "
			},
			"1247": {
				"cn": " 采购材料、设备质量管理 ",
				"en": " Supplies & Equipment Quality Management "
			},
			"1248": {
				"cn": " 安全防护 ",
				"en": " Safety Protection "
			},
			"1249": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1018": {
			"1250": {
				"cn": " 技术研发经理/主管 ",
				"en": " Technical Design Mgr./Spvr. "
			},
			"1251": {
				"cn": " 技术研发工程师 ",
				"en": " Technical Design Engineer "
			},
			"1252": {
				"cn": " 产品工艺/制程工程师 ",
				"en": " Process Engineer "
			},
			"1253": {
				"cn": " 产品规划工程师 ",
				"en": " Product Planing Engineer "
			},
			"1254": {
				"cn": " 项目管理 ",
				"en": " Project Management "
			},
			"1255": {
				"cn": " 实验室负责人/工程师 ",
				"en": " Lab Manager/Engineer "
			},
			"1256": {
				"cn": " 工程/设备经理 ",
				"en": " Engineering/Facility Manager "
			},
			"1257": {
				"cn": " 工程/设备主管 ",
				"en": " Engineering/Facility Supervisor "
			},
			"1258": {
				"cn": " 工程/设备工程师 ",
				"en": " Engineering/Facility Engineer "
			},
			"1259": {
				"cn": " 工程/机械绘图员 ",
				"en": " Project Drafting Specialist/Mechanical Drawing "
			},
			"1260": {
				"cn": " 工业工程师 ",
				"en": " Industrial Engineer "
			},
			"1261": {
				"cn": " 材料工程师 ",
				"en": " Material Engineer "
			},
			"1262": {
				"cn": " 机械工程师 ",
				"en": " Mechanical Engineer "
			},
			"1263": {
				"cn": " 结构工程师 ",
				"en": " Structrual Engineer "
			},
			"1264": {
				"cn": " 模具工程师 ",
				"en": " Tooling Engineer "
			},
			"1265": {
				"cn": " 机电工程师 ",
				"en": " Electrical & Mechanical Engineer "
			},
			"1266": {
				"cn": " 维修经理/主管 ",
				"en": " Maintenance Manager/Supervisor "
			},
			"1267": {
				"cn": " 维修工程师 ",
				"en": " Maintenance Engineer "
			},
			"1268": {
				"cn": " 装配工程师/技师 ",
				"en": " Packaging&Assembly Engineer "
			},
			"1269": {
				"cn": " 铸造/锻造工程师/技师 ",
				"en": " Casting/Forging Engineer "
			},
			"1270": {
				"cn": " 注塑工程师/技师 ",
				"en": " Injection Engineer "
			},
			"1271": {
				"cn": " 焊接工程师/技师 ",
				"en": " Welding Engineer "
			},
			"1272": {
				"cn": " 夹具工程师/技师 ",
				"en": " Clamp Engineer "
			},
			"1273": {
				"cn": " CNC工程师 ",
				"en": " CNC Engineer "
			},
			"1274": {
				"cn": " 冲压工程师/技师 ",
				"en": " Punch Engineer "
			},
			"1275": {
				"cn": " 锅炉工程师/技师 ",
				"en": " Boiler Engineer "
			},
			"1276": {
				"cn": " 电力工程师/技术员 ",
				"en": " Electric Power Engineer "
			},
			"1277": {
				"cn": " 光源与照明工程 ",
				"en": " Lighting Engineer "
			},
			"1278": {
				"cn": " 光伏系统工程师 ",
				"en": " Photovoltaic System Engineer "
			},
			"1279": {
				"cn": " 汽车/摩托车工程师 ",
				"en": " Automotive Engineer "
			},
			"1280": {
				"cn": " 船舶工程师 ",
				"en": " Shipping Engineer "
			},
			"1281": {
				"cn": " 轨道交通工程师/技术员 ",
				"en": " Railway Engineer / Technician "
			},
			"1282": {
				"cn": " 飞机维修机械师 ",
				"en": " Aviation Maintenance Technician "
			},
			"1283": {
				"cn": " 飞行器设计与制造 ",
				"en": " Aircraft Design & Manufacture "
			},
			"1284": {
				"cn": " 水利/水电工程师 ",
				"en": " Water Conservancy/Hydroelectricity Engineer "
			},
			"1285": {
				"cn": " 石油天然气技术人员 ",
				"en": " Oil/Gas Technician "
			},
			"1286": {
				"cn": " 矿产勘探/地质勘测工程师 ",
				"en": " Mineral Exploration / Geological Survey Engineer "
			},
			"1287": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1019": {
			"1288": {
				"cn": " 汽车机构工程师 ",
				"en": " Automotive Structural Engineer "
			},
			"1289": {
				"cn": " 汽车设计工程师 ",
				"en": " Automotive Design Engineer "
			},
			"1290": {
				"cn": " 汽车电子工程师 ",
				"en": " Automotive Electronics Engineer "
			},
			"1291": {
				"cn": " 汽车质量管理 ",
				"en": " Automotive Quality Management "
			},
			"1292": {
				"cn": " 汽车安全性能工程师 ",
				"en": " Safety Performance Engineer "
			},
			"1293": {
				"cn": " 汽车装配工艺工程师 ",
				"en": " Assembly Process Engineer "
			},
			"1294": {
				"cn": " 汽车修理人员 ",
				"en": " Automotive Repair "
			},
			"1295": {
				"cn": " 4S店经理/维修站经理 ",
				"en": " 4S Shop Manager / Maintenance Station Manager "
			},
			"1296": {
				"cn": " 汽车销售/经纪人 ",
				"en": " Automotive Sales Consultant / Brokers "
			},
			"1297": {
				"cn": " 二手车评估师 ",
				"en": " Second-Hand Car Appraisers "
			},
			"1298": {
				"cn": " 汽车项目管理 ",
				"en": " Automotive Project Management "
			},
			"1299": {
				"cn": " 售后服务/客户服务 ",
				"en": " After-Sales Service/Customer Service "
			},
			"1300": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1020": {
			"1301": {
				"cn": " 技工 ",
				"en": " Technician / Engineer Trainee "
			},
			"1302": {
				"cn": " 钳工/机修工/钣金工 ",
				"en": " Locksmith/Mechanic/Repairer "
			},
			"1303": {
				"cn": " 电焊工/铆焊工 ",
				"en": " Electric Welding Worker "
			},
			"1304": {
				"cn": " 车工/磨工/铣工/冲压工/锣工 ",
				"en": " Latheman/Grinder/Miller/Puncher/Turner "
			},
			"1305": {
				"cn": " 模具工 ",
				"en": " Mould Worker "
			},
			"1306": {
				"cn": " 电工 ",
				"en": " Electrician "
			},
			"1307": {
				"cn": " 叉车工 ",
				"en": " Forklift Worker "
			},
			"1308": {
				"cn": " 空调工/电梯工/锅炉工 ",
				"en": " Air-Condition Worker/Lift Worker/Steam Worker "
			},
			"1309": {
				"cn": " 水工/木工/漆工 ",
				"en": " Plumber/Carpenter/Painter "
			},
			"1310": {
				"cn": " 普工/操作工 ",
				"en": " General Worker "
			},
			"1311": {
				"cn": " 裁缝印纺熨烫 ",
				"en": " Tailor "
			},
			"1312": {
				"cn": " 汽车修理工 ",
				"en": " Auto Repairing "
			},
			"1313": {
				"cn": " 切割技工 ",
				"en": " Cutting Technician "
			},
			"1314": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1021": {
			"1315": {
				"cn": " 服装/纺织设计 ",
				"en": " Fashion/Textiles Designer "
			},
			"1316": {
				"cn": " 面料辅料开发 ",
				"en": " Fabric/Accessories Development "
			},
			"1317": {
				"cn": " 面料辅料采购 ",
				"en": " Fabric/Accessories Purchasing "
			},
			"1318": {
				"cn": " 服装/纺织/皮革跟单 ",
				"en": " Apparels/Textiles/Leather Goods Merchandiser "
			},
			"1319": {
				"cn": " 质量管理/验货员(QA/QC) ",
				"en": " Quality Management QA/QC "
			},
			"1320": {
				"cn": " 板房/楦头/底格出格师 ",
				"en": " Shoe Tree Design "
			},
			"1321": {
				"cn": " 打样/制版 ",
				"en": " Sample Production "
			},
			"1322": {
				"cn": " 纸样师/车板工 ",
				"en": " Paper Sample "
			},
			"1323": {
				"cn": " 裁床 ",
				"en": " Cut Bed "
			},
			"1324": {
				"cn": " 电脑放码员 ",
				"en": " Grading "
			},
			"1325": {
				"cn": " 服装/纺织设计总监 ",
				"en": " Fashion/Textiles Design Director "
			},
			"1326": {
				"cn": " 服装/纺织/皮革工艺师 ",
				"en": " Fashion/Textiles/Leather Technologist "
			},
			"1327": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1022": {
			"1328": {
				"cn": " 采购总监 ",
				"en": " Purchasing Director "
			},
			"1329": {
				"cn": " 采购经理 ",
				"en": " Purchasing Manager "
			},
			"1330": {
				"cn": " 采购主管 ",
				"en": " Purchasing Supervisor "
			},
			"1331": {
				"cn": " 采购员 ",
				"en": " Purchasing Specialist/Staff "
			},
			"1332": {
				"cn": " 采购助理 ",
				"en": " Purchasing Assistant "
			},
			"1333": {
				"cn": " 买手 ",
				"en": " Buyer "
			},
			"1334": {
				"cn": " 供应商开发 ",
				"en": " Supplier Development "
			},
			"1335": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1023": {
			"1336": {
				"cn": " 贸易/外贸经理/主管 ",
				"en": " Trading/Manager/Supervisor "
			},
			"1337": {
				"cn": " 贸易/外贸专员/助理 ",
				"en": " Trading/Specialist/Assistant "
			},
			"1338": {
				"cn": " 国内贸易人员 ",
				"en": " Domestic Trade Specialist "
			},
			"1339": {
				"cn": " 业务跟单经理 ",
				"en": " Merchandising Manager "
			},
			"1340": {
				"cn": " 高级业务跟单 ",
				"en": " Senior Merchandiser "
			},
			"1341": {
				"cn": " 业务跟单 ",
				"en": " Merchandiser "
			},
			"1342": {
				"cn": " 助理业务跟单 ",
				"en": " Assistant Merchandiser "
			},
			"1343": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1024": {
			"1344": {
				"cn": " 物流总监 ",
				"en": " Logistics Director "
			},
			"1345": {
				"cn": " 物流经理 ",
				"en": " Logistics Manager "
			},
			"1346": {
				"cn": " 物流主管 ",
				"en": " Logistics Supervisor "
			},
			"1347": {
				"cn": " 物流专员/助理 ",
				"en": " Logistics Specialist/Assistant "
			},
			"1348": {
				"cn": " 供应链总监 ",
				"en": " Supply Chain Director "
			},
			"1349": {
				"cn": " 供应链经理 ",
				"en": " Supply Chain Manager "
			},
			"1350": {
				"cn": " 供应链主管/专员 ",
				"en": " Supply Chain Supervisor/Specialist "
			},
			"1351": {
				"cn": " 物料经理 ",
				"en": " Materials Manager "
			},
			"1352": {
				"cn": " 物料主管/专员 ",
				"en": " Materials Supervisor/Specialist "
			},
			"1353": {
				"cn": " 仓库经理/主管 ",
				"en": " Warehouse Manager "
			},
			"1354": {
				"cn": " 仓库管理员 ",
				"en": " Warehouse Specialist "
			},
			"1355": {
				"cn": " 运输经理/主管 ",
				"en": " Distribution Manager/Supervisor "
			},
			"1356": {
				"cn": " 项目经理/主管 ",
				"en": " Project Manager/Supervisor "
			},
			"1357": {
				"cn": " 货运代理 ",
				"en": " Traffic Agent "
			},
			"1358": {
				"cn": " 集装箱业务 ",
				"en": " Container Operator "
			},
			"1359": {
				"cn": " 海关事务管理 ",
				"en": " Customs Affairs Management "
			},
			"1360": {
				"cn": " 报关与报检 ",
				"en": " Customs Specialist "
			},
			"1361": {
				"cn": " 单证员 ",
				"en": " Documentation Specialist "
			},
			"1362": {
				"cn": " 船务/空运陆运操作 ",
				"en": " Shipping Specialist "
			},
			"1363": {
				"cn": " 快递员 ",
				"en": " Courier "
			},
			"1364": {
				"cn": " 调度员 ",
				"en": " Dispatcher "
			},
			"1365": {
				"cn": " 理货员 ",
				"en": " Warehouse Stock Management "
			},
			"1366": {
				"cn": " 其他 ",
				"en": " Others "
			}
		}
	},
	"1005": {
		"1025": {
			"1367": {
				"cn": " 生物工程/生物制药 ",
				"en": " Biotechnology/Pharmaceuticals "
			},
			"1368": {
				"cn": " 医药技术研发管理人员 ",
				"en": " Pharmaceutical Technology R&D Management "
			},
			"1369": {
				"cn": " 医药技术研发人员 ",
				"en": " Pharmaceutical Technology R&D Specialist "
			},
			"1370": {
				"cn": " 临床研究员 ",
				"en": " Clinical Researcher "
			},
			"1371": {
				"cn": " 临床协调员 ",
				"en": " Clinical Coodinator "
			},
			"1372": {
				"cn": " 药品注册 ",
				"en": " Pharmaceuticals Register Specialist "
			},
			"1373": {
				"cn": " 药品生产/质量管理 ",
				"en": " Pharmaceutical Manufacturing/Quality Management "
			},
			"1374": {
				"cn": " 药品市场推广经理 ",
				"en": " Pharmaceutical Marketing Manager "
			},
			"1375": {
				"cn": " 药品市场推广主管/专员 ",
				"en": " Pharmaceutical Marketing Supervisor/Specialist "
			},
			"1376": {
				"cn": " 医药销售经理/主管 ",
				"en": " Pharmaceutical Sales Manager "
			},
			"1377": {
				"cn": " 医药销售代表 ",
				"en": " Pharmaceutical Sales Representative "
			},
			"1378": {
				"cn": " 医疗器械市场推广 ",
				"en": " Medical Equipment Marketing "
			},
			"1379": {
				"cn": " 医疗器械销售代表 ",
				"en": " Medical Equipment Sales "
			},
			"1380": {
				"cn": " 化学分析测试员 ",
				"en": " Chemical Analyst "
			},
			"1381": {
				"cn": " 医疗器械注册 ",
				"en": " Medical Equipment Registration "
			},
			"1382": {
				"cn": " 医疗器械生产/质量管理 ",
				"en": " Medical Equipment Manufacturing/Quality Control "
			},
			"1383": {
				"cn": " 医疗器械维修人员 ",
				"en": " Medical Equipment Maintenance Engineer "
			},
			"1384": {
				"cn": " 医药招商 ",
				"en": " Pharmaceutical Business Development "
			},
			"1385": {
				"cn": " 政府事务管理 ",
				"en": " Government Affairs "
			},
			"1386": {
				"cn": " 招投标管理 ",
				"en": " Tendering Coordinator "
			},
			"1387": {
				"cn": " 临床数据分析员 ",
				"en": " Clinical Data Analyst "
			},
			"1388": {
				"cn": " 医疗器械研发 ",
				"en": " Medical Equipment R&D "
			},
			"1389": {
				"cn": " 医疗器械销售经理/主管 ",
				"en": " Medical Equipment Sales Manager/Supervisor "
			},
			"1390": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1026": {
			"1391": {
				"cn": " 化工技术应用/化工工程师 ",
				"en": " Chemical Technical Application/Chemical Engineer "
			},
			"1392": {
				"cn": " 化工实验室研究员/技术员 ",
				"en": " Chemical Lab Scientist / Technician "
			},
			"1393": {
				"cn": " 涂料研发工程师 ",
				"en": " R&D Chemist Scientist "
			},
			"1394": {
				"cn": " 配色技术员 ",
				"en": " Color Matcher (Technician) "
			},
			"1395": {
				"cn": " 塑料工程师 ",
				"en": " Plastics Engineer "
			},
			"1396": {
				"cn": " 化妆品研发 ",
				"en": " Cosmetics Scientist "
			},
			"1397": {
				"cn": " 食品/饮料研发 ",
				"en": " Food / Beverage Scientist "
			},
			"1398": {
				"cn": " 造纸研发 ",
				"en": " Paper Making Scientist "
			},
			"1399": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1027": {
			"1400": {
				"cn": " 内科医生 ",
				"en": " Doctor, Internal Medicine "
			},
			"1401": {
				"cn": " 医院管理人员 ",
				"en": " Hospital Management "
			},
			"1402": {
				"cn": " 药库主任/药剂师 ",
				"en": " Pharmacist "
			},
			"1403": {
				"cn": " 护士/护理人员 ",
				"en": " Nurse/Medical Assistant "
			},
			"1404": {
				"cn": " 麻醉医生 ",
				"en": " Anesthesiologist "
			},
			"1405": {
				"cn": " 心理医生 ",
				"en": " Psychologist/Psychiatrist "
			},
			"1406": {
				"cn": " 医药学检验 ",
				"en": " Clinical Laboratory "
			},
			"1407": {
				"cn": " 针灸、推拿 ",
				"en": " Acupuncturist "
			},
			"1408": {
				"cn": " 营养师 ",
				"en": " Dietitian "
			},
			"1409": {
				"cn": " 兽医 ",
				"en": " Veterinarian "
			},
			"1410": {
				"cn": " 外科医生 ",
				"en": " Doctor, Surgeial "
			},
			"1411": {
				"cn": " 专科医生 ",
				"en": " Doctor, Specialist "
			},
			"1412": {
				"cn": " 牙科医生 ",
				"en": " Dentist "
			},
			"1413": {
				"cn": " 美容整形师 ",
				"en": " Plastic Surgeon "
			},
			"1414": {
				"cn": " 理疗师 ",
				"en": " Physical Therapist "
			},
			"1415": {
				"cn": " 中医科医生 ",
				"en": " Chinese Medicine Practioners "
			},
			"1416": {
				"cn": " 公共卫生/疾病控制 ",
				"en": " Public Sanitation/Disease Control "
			},
			"1417": {
				"cn": " 护理主任/护士长 ",
				"en": " Nursing Officer "
			},
			"1418": {
				"cn": " 儿科医生 ",
				"en": " Pediatrician "
			},
			"1419": {
				"cn": " 验光师 ",
				"en": " Optometrist "
			},
			"1420": {
				"cn": " 放射科医师 ",
				"en": " Radiologist "
			},
			"1421": {
				"cn": " 其他 ",
				"en": " Others "
			}
		}
	},
	"1006": {
		"1028": {
			"1422": {
				"cn": " 广告客户总监/副总监 ",
				"en": " Advertising Account Director/Associate Director "
			},
			"1423": {
				"cn": " 广告客户经理 ",
				"en": " Advertising Account Manager "
			},
			"1424": {
				"cn": " 广告客户主管/专员 ",
				"en": " Advertising Account Supervisor/Executive "
			},
			"1425": {
				"cn": " 广告创意/设计经理 ",
				"en": " Advertising Creative/Design Manager "
			},
			"1426": {
				"cn": " 广告创意总监 ",
				"en": " Advertising Creative Director "
			},
			"1427": {
				"cn": " 广告创意/设计主管/专员 ",
				"en": " Advertising Creative/Design Supervisor/Executive "
			},
			"1428": {
				"cn": " 文案/策划 ",
				"en": " Copywriter/Planner "
			},
			"1429": {
				"cn": " 企业/业务发展经理 ",
				"en": " Business Development Manager "
			},
			"1430": {
				"cn": " 企业策划人员 ",
				"en": " Business Planning Staff "
			},
			"1431": {
				"cn": " 美术指导 ",
				"en": " Art Director "
			},
			"1432": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1029": {
			"1433": {
				"cn": " 公关经理 ",
				"en": " Public Relations Manager "
			},
			"1434": {
				"cn": " 公关主管 ",
				"en": " Public Relations Supervisor "
			},
			"1435": {
				"cn": " 公关专员 ",
				"en": " Public Relations Executive "
			},
			"1436": {
				"cn": " 会务/会展经理 ",
				"en": " Exhibition/Event Manager "
			},
			"1437": {
				"cn": " 会务/会展主管 ",
				"en": " Exhibition/Event Supervisor "
			},
			"1438": {
				"cn": " 会务/会展专员 ",
				"en": " Exhibition/Event Executive "
			},
			"1439": {
				"cn": " 媒介经理 ",
				"en": " Media Manager "
			},
			"1440": {
				"cn": " 媒介主管 ",
				"en": " Media Supervisor "
			},
			"1441": {
				"cn": " 媒介专员 ",
				"en": " Media Specialist "
			},
			"1442": {
				"cn": " 公关/媒介助理 ",
				"en": " Public Relations/Media Assistant "
			},
			"1443": {
				"cn": " 媒介销售 ",
				"en": " Media Sales "
			},
			"1444": {
				"cn": " 活动策划 ",
				"en": " Event Planner "
			},
			"1445": {
				"cn": " 活动执行 ",
				"en": " Event Excution "
			},
			"1446": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1030": {
			"1447": {
				"cn": " 市场/营销/拓展总监 ",
				"en": " Marketing / BD Director / VP "
			},
			"1448": {
				"cn": " 市场/营销/拓展经理 ",
				"en": " Marketing / BD  Manager "
			},
			"1449": {
				"cn": " 市场/营销/拓展主管 ",
				"en": " Marketing  / BD Supervisor "
			},
			"1450": {
				"cn": " 市场/营销/拓展专员 ",
				"en": " Marketing  / BD Executive/Communication "
			},
			"1451": {
				"cn": " 市场助理 ",
				"en": " Marketing Assistant / Trainee "
			},
			"1452": {
				"cn": " 市场分析/调研人员 ",
				"en": " Market Analyst/ Research Analyst "
			},
			"1453": {
				"cn": " 产品/品牌经理 ",
				"en": " Product/Brand Manager "
			},
			"1454": {
				"cn": " 产品/品牌主管 ",
				"en": " Product/Brand Supervisor "
			},
			"1455": {
				"cn": " 产品/品牌专员 ",
				"en": " Product/Brand Executive "
			},
			"1456": {
				"cn": " 市场通路经理/主管 ",
				"en": " Trade Marketing Manager/Supervisor "
			},
			"1457": {
				"cn": " 市场通路专员 ",
				"en": " Trade Marketing Specialist "
			},
			"1458": {
				"cn": " 市场企划经理/主管 ",
				"en": " Marketing Planning Manager/Supervisor "
			},
			"1459": {
				"cn": " 市场企划专员 ",
				"en": " Marketing Planning Executive "
			},
			"1460": {
				"cn": " 促销经理 ",
				"en": " Promotion Manager "
			},
			"1461": {
				"cn": " 促销主管/督导 ",
				"en": " Promotion Supervisor "
			},
			"1462": {
				"cn": " 促销员/导购 ",
				"en": " Promotion Specialist "
			},
			"1463": {
				"cn": " 选址拓展/新店开发 ",
				"en": " Site Development "
			},
			"1464": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1031": {
			"1465": {
				"cn": " 影视策划/制作人员 ",
				"en": " Entertainment /Produer "
			},
			"1466": {
				"cn": " 导演/编导 ",
				"en": " Director "
			},
			"1467": {
				"cn": " 艺术/设计总监 ",
				"en": " Artistic/Design Director "
			},
			"1468": {
				"cn": " 经纪人/星探 ",
				"en": " Entertainment Agent "
			},
			"1469": {
				"cn": " 演员/模特/主持人 ",
				"en": " Actor/Actress/Model/MC "
			},
			"1470": {
				"cn": " 摄影师/摄像师 ",
				"en": " Photographer "
			},
			"1471": {
				"cn": " 音效师 ",
				"en": " Recording / Sounds Specialist "
			},
			"1472": {
				"cn": " 配音员 ",
				"en": " Dubbing Specialist "
			},
			"1473": {
				"cn": " 化妆师/造型师 ",
				"en": " Makeup Artist/Image Designer "
			},
			"1474": {
				"cn": " 后期制作 ",
				"en": " Postproduction "
			},
			"1475": {
				"cn": " 放映经理/主管 ",
				"en": " Projection Manager/Supervisor "
			},
			"1476": {
				"cn": " 放映员 ",
				"en": " Projectionist "
			},
			"1477": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1032": {
			"1478": {
				"cn": " 总编/副总编 ",
				"en": " Chief Editor "
			},
			"1479": {
				"cn": " 编辑 ",
				"en": " Editor "
			},
			"1480": {
				"cn": " 记者 ",
				"en": " Journalist / Reporter "
			},
			"1481": {
				"cn": " 美术编辑 ",
				"en": " Art Editor "
			},
			"1482": {
				"cn": " 排版设计 ",
				"en": " Layout Designer "
			},
			"1483": {
				"cn": " 校对/录入 ",
				"en": " Proofreader/Data Entry Staff "
			},
			"1484": {
				"cn": " 出版/发行 ",
				"en": " Publishing/Distribution "
			},
			"1485": {
				"cn": " 电分操作员 ",
				"en": " Operator-Colour Distinguishing "
			},
			"1486": {
				"cn": " 印刷排版/制版 ",
				"en": " Layout Designer "
			},
			"1487": {
				"cn": " 数码直印/菲林输出 ",
				"en": " Digital/Film Printing "
			},
			"1488": {
				"cn": " 打稿机操作员 ",
				"en": " Operator "
			},
			"1489": {
				"cn": " 调墨技师 ",
				"en": " Ink Technician "
			},
			"1490": {
				"cn": " 印刷机械机长 ",
				"en": " Printing Machine Operator "
			},
			"1491": {
				"cn": " 晒版/拼版/装订/烫金技工 ",
				"en": " Technician "
			},
			"1492": {
				"cn": " 电话采编 ",
				"en": " Telephone Reporter "
			},
			"1493": {
				"cn": " 作家/撰稿人 ",
				"en": " Writer "
			},
			"1494": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1033": {
			"1495": {
				"cn": " 平面设计总监 ",
				"en": " Graphic Design Director "
			},
			"1496": {
				"cn": " 平面设计经理/主管 ",
				"en": " Graphic Design Manager/Supervisor "
			},
			"1497": {
				"cn": " 平面设计师 ",
				"en": " Graphic Artist/Designer "
			},
			"1498": {
				"cn": " 绘画 ",
				"en": " Graphic Illustrator "
			},
			"1499": {
				"cn": " 动画/3D设计 ",
				"en": " Animation/3D Design "
			},
			"1500": {
				"cn": " 原画师 ",
				"en": " Original Artist "
			},
			"1501": {
				"cn": " 展览/展示/店面设计 ",
				"en": " Exhibition/Display/Storefront Design "
			},
			"1502": {
				"cn": " 多媒体设计 ",
				"en": " Multimedia Design "
			},
			"1503": {
				"cn": " 包装设计 ",
				"en": " Package Design "
			},
			"1504": {
				"cn": " 工业/产品设计 ",
				"en": " Industrial Designer "
			},
			"1505": {
				"cn": " 工艺品/珠宝设计鉴定 ",
				"en": " Artwork/Jewelry Design and Appraisal "
			},
			"1506": {
				"cn": " 家具/家居用品设计 ",
				"en": " Furniture/Household Product Design "
			},
			"1507": {
				"cn": " 玩具设计 ",
				"en": " Toy Design "
			},
			"1508": {
				"cn": " 其他 ",
				"en": " Others "
			}
		}
	},
	"1007": {
		"1034": {
			"1509": {
				"cn": " 建筑工程师 ",
				"en": " Architect "
			},
			"1510": {
				"cn": " 结构/土木/土建工程师 ",
				"en": " Structural Engineer "
			},
			"1511": {
				"cn": " 建筑机电工程师 ",
				"en": " Building Electrical Engineer "
			},
			"1512": {
				"cn": " 给排水/暖通工程 ",
				"en": " Drainage/HVAC Project Engineer "
			},
			"1513": {
				"cn": " 工程造价师/预结算经理 ",
				"en": " Project Estimator "
			},
			"1514": {
				"cn": " 建筑工程管理/项目经理 ",
				"en": " Construction Project Management "
			},
			"1515": {
				"cn": " 工程监理 ",
				"en": " Engineering Project Supervisor "
			},
			"1516": {
				"cn": " 室内设计 ",
				"en": " Interior Design/Drchitectural Drawing "
			},
			"1517": {
				"cn": " 规划与设计 ",
				"en": " Design/Planning "
			},
			"1518": {
				"cn": " 建筑制图/模型/渲染 ",
				"en": " CAD Drafter/Building Model/Rendering "
			},
			"1519": {
				"cn": " 施工员 ",
				"en": " Construction Crew "
			},
			"1520": {
				"cn": " 园艺/园林/景观设计 ",
				"en": " Gardenning Designer "
			},
			"1521": {
				"cn": " 公路/桥梁/港口/隧道工程 ",
				"en": " Road/Bridge/Port/Tunnel Project Engineer "
			},
			"1522": {
				"cn": " 岩土工程 ",
				"en": " Geotechnical Engineer "
			},
			"1523": {
				"cn": " 测绘/测量 ",
				"en": " Mapping/Surveyor "
			},
			"1524": {
				"cn": " 建筑工程验收 ",
				"en": " Construction Project Inspector "
			},
			"1525": {
				"cn": " 幕墙工程师 ",
				"en": " Curtain Wall Engineer "
			},
			"1526": {
				"cn": " 高级建筑工程师/总工 ",
				"en": " Senior Architect "
			},
			"1527": {
				"cn": " 预结算员 ",
				"en": " Quantity Surveyor "
			},
			"1528": {
				"cn": " 楼宇自动化 ",
				"en": " Building Automation "
			},
			"1529": {
				"cn": " 智能大厦/综合布线/安防/弱电 ",
				"en": " Intelligent Building/Integrated Wiring/Defence&Security/Weak Current "
			},
			"1530": {
				"cn": " 开发报建 ",
				"en": " Programming&Applying for Building "
			},
			"1531": {
				"cn": " 合同管理 ",
				"en": " Contract Management "
			},
			"1532": {
				"cn": " 安全员 ",
				"en": " Safety Specialist "
			},
			"1533": {
				"cn": " 资料员 ",
				"en": " Data Management Specialist "
			},
			"1534": {
				"cn": " 建筑设计师 ",
				"en": " Architectural Designer "
			},
			"1535": {
				"cn": " 市政工程师 ",
				"en": " Municipal Project Engineer "
			},
			"1536": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1035": {
			"1537": {
				"cn": " 房地产项目/开发/策划经理 ",
				"en": " Real Estate Project/Development/Planning Manager "
			},
			"1538": {
				"cn": " 房地产项目/开发/策划主管/专员 ",
				"en": " Real Estate Project/Development/Planning Supervisor/Specialist "
			},
			"1539": {
				"cn": " 房产项目配套工程师 ",
				"en": " Conveyance System Engineer "
			},
			"1540": {
				"cn": " 房地产评估 ",
				"en": " Real Estate Appraisal "
			},
			"1541": {
				"cn": " 房地产中介/交易 ",
				"en": " Real Estate Agent/Broker "
			},
			"1542": {
				"cn": " 房地产销售人员 ",
				"en": " Real Estate Sales "
			},
			"1543": {
				"cn": " 房地产项目招投标 ",
				"en": " Real Estate Tender /Bidding "
			},
			"1544": {
				"cn": " 房地产销售经理/主管 ",
				"en": " Real Estate Sales Manager/Supervisor "
			},
			"1545": {
				"cn": " 房地产投资分析 ",
				"en": " Real Estate Investment Analysis "
			},
			"1546": {
				"cn": " 房地产资产管理 ",
				"en": " Real Estate Asset Management "
			},
			"1547": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1036": {
			"1548": {
				"cn": " 高级物业顾问/物业顾问 ",
				"en": " Senior Property Advisor/Property Advisor "
			},
			"1549": {
				"cn": " 物业管理经理/主管 ",
				"en": " Property Management Manager/Supervisor "
			},
			"1550": {
				"cn": " 物业管理专员/助理 ",
				"en": " Property Management "
			},
			"1551": {
				"cn": " 物业招商/租赁/租售 ",
				"en": " Property Lease/Rent "
			},
			"1552": {
				"cn": " 物业设施管理人员 ",
				"en": " Property Establishment Management "
			},
			"1553": {
				"cn": " 物业维修人员 ",
				"en": " Property Maintainence Staff "
			},
			"1554": {
				"cn": " 物业机电工程师 ",
				"en": " Property Mechanical Engineer "
			},
			"1555": {
				"cn": " 其他 ",
				"en": " Others "
			}
		}
	},
	"1008": {
		"1037": {
			"1556": {
				"cn": " 人事总监 ",
				"en": " Human Resources Director "
			},
			"1557": {
				"cn": " 人事经理 ",
				"en": " Human Resources Manager "
			},
			"1558": {
				"cn": " 人事主管 ",
				"en": " Human Resources Supervisor "
			},
			"1559": {
				"cn": " 人事专员 ",
				"en": " Human Resources Specialist "
			},
			"1560": {
				"cn": " 人事助理 ",
				"en": " Human Resources Assistant "
			},
			"1561": {
				"cn": " 招聘经理/主管 ",
				"en": " Recruiting Manager/Supervisor "
			},
			"1562": {
				"cn": " 招聘专员/助理 ",
				"en": " Recruiting Specialist/Assistant "
			},
			"1563": {
				"cn": " 薪资福利经理/主管 ",
				"en": " Compensation & Benefits Mgr./Supervisor "
			},
			"1564": {
				"cn": " 薪资福利专员/助理 ",
				"en": " Compensation & Benefits Specialist/Assistant "
			},
			"1565": {
				"cn": " 绩效考核经理/主管 ",
				"en": " Performance Assessment Manager/Supervisor "
			},
			"1566": {
				"cn": " 绩效考核专员/助理 ",
				"en": " Performance Assessment Specialist/Assistant "
			},
			"1567": {
				"cn": " 培训经理/主管 ",
				"en": " Training Manager/Supervisor "
			},
			"1568": {
				"cn": " 培训专员/助理/培训师 ",
				"en": " Training Specialist/Assistant/Trainer "
			},
			"1569": {
				"cn": " 企业文化/员工关系/工会管理 ",
				"en": " Corporate Culture/Employee Labor Union Relations "
			},
			"1570": {
				"cn": " 人力资源信息系统专员 ",
				"en": " HRIS Specialist "
			},
			"1571": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1038": {
			"1572": {
				"cn": " 首席执行官CEO/总裁/总经理 ",
				"en": " CEO/President/General Manager "
			},
			"1573": {
				"cn": " 首席运营官COO ",
				"en": " COO "
			},
			"1574": {
				"cn": " 副总经理/副总裁 ",
				"en": " Deputy GM/Vice President "
			},
			"1575": {
				"cn": " 合伙人 ",
				"en": " Partner "
			},
			"1576": {
				"cn": " 总监/部门经理 ",
				"en": " Director/Department Manager "
			},
			"1577": {
				"cn": " 策略发展总监 ",
				"en": " Strategic Planning Director "
			},
			"1578": {
				"cn": " 企业秘书/董事会秘书 ",
				"en": " Corporate/Board Secretary "
			},
			"1579": {
				"cn": " 投资者关系 ",
				"en": " Investor Relations "
			},
			"1580": {
				"cn": " 办事处首席代表 ",
				"en": " Chief Representative "
			},
			"1581": {
				"cn": " 办事处/分公司/分支机构经理 ",
				"en": " Branch Office Manager "
			},
			"1582": {
				"cn": " 总裁助理/总经理助理 ",
				"en": " CEO/GM/President Assistant "
			},
			"1583": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1039": {
			"1584": {
				"cn": " 行政总监 ",
				"en": " Admin Director "
			},
			"1585": {
				"cn": " 行政经理/主管/办公室主任 ",
				"en": " Admin Manager/Supervisor/Office Manager "
			},
			"1586": {
				"cn": " 行政专员/助理 ",
				"en": " Admin Staff/Assistant "
			},
			"1587": {
				"cn": " 经理助理/秘书 ",
				"en": " Executive Assistant/Secretary "
			},
			"1588": {
				"cn": " 前台接待/总机/接待生 ",
				"en": " Receptionist "
			},
			"1589": {
				"cn": " 后勤 ",
				"en": " Office Support "
			},
			"1590": {
				"cn": " 图书管理员/资料管理员 ",
				"en": " Librarian / Information/Data Management Specialist "
			},
			"1591": {
				"cn": " 电脑操作员/打字员 ",
				"en": " Computer Operator/Typist "
			},
			"1592": {
				"cn": " 其他 ",
				"en": " Others "
			}
		}
	},
	"1009": {
		"1040": {
			"1593": {
				"cn": " 专业顾问 ",
				"en": " Senior Consultant "
			},
			"1594": {
				"cn": " 咨询总监 ",
				"en": " Consulting Director / Partner "
			},
			"1595": {
				"cn": " 咨询经理 ",
				"en": " Consulting Manager "
			},
			"1596": {
				"cn": " 咨询员 ",
				"en": " Consultant "
			},
			"1597": {
				"cn": " 专业培训师 ",
				"en": " Professional Trainer "
			},
			"1598": {
				"cn": " 情报信息分析人员 ",
				"en": " Market Intelligence Analyst "
			},
			"1599": {
				"cn": " 猎头/人才中介 ",
				"en": " Headhunting "
			},
			"1600": {
				"cn": " 调研员 ",
				"en": " Research Analyst "
			},
			"1601": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1041": {
			"1602": {
				"cn": " 律师/法律顾问 ",
				"en": " Lawyer/Counsel "
			},
			"1603": {
				"cn": " 法务主管/专员 ",
				"en": " Legal Supervisor/Specialist "
			},
			"1604": {
				"cn": " 律师助理 ",
				"en": " Paralegal "
			},
			"1605": {
				"cn": " 法务经理 ",
				"en": " Corporate Counsel/Compliance Officer "
			},
			"1606": {
				"cn": " 法务助理 ",
				"en": " Legal Assistant "
			},
			"1607": {
				"cn": " 知识产权/专利/商标 ",
				"en": " Intellectual Property/Patent Advisor/Trademark "
			},
			"1608": {
				"cn": " 合规经理 ",
				"en": " Compliance Manager "
			},
			"1609": {
				"cn": " 合规主管/专员 ",
				"en": " Compliance Supervisor/Specialist "
			},
			"1610": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1042": {
			"1611": {
				"cn": " 中学教师 ",
				"en": " High School Teacher "
			},
			"1612": {
				"cn": " 院校教务管理人员 ",
				"en": " Educational Facility Management "
			},
			"1613": {
				"cn": " 讲师/助教 ",
				"en": " Lecturer/Teaching Assistant "
			},
			"1614": {
				"cn": " 家教 ",
				"en": " Tutor "
			},
			"1615": {
				"cn": " 幼教 ",
				"en": " Preschool Education "
			},
			"1616": {
				"cn": " 大学教授 ",
				"en": " Professor "
			},
			"1617": {
				"cn": " 小学教师 ",
				"en": " Grade School Teacher "
			},
			"1618": {
				"cn": " 兼职教师 ",
				"en": " Part-time Teacher "
			},
			"1619": {
				"cn": " 职业技术教师 ",
				"en": " Vocational Instructor "
			},
			"1620": {
				"cn": " 校长 ",
				"en": " School Principal "
			},
			"1621": {
				"cn": " 音乐/美术教师 ",
				"en": " Music/Art Teacher "
			},
			"1622": {
				"cn": " 外语培训师 ",
				"en": " Foreign Language Instructor "
			},
			"1623": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1043": {
			"1624": {
				"cn": " 培训督导 ",
				"en": " Supervision Training "
			},
			"1625": {
				"cn": " 培训讲师 ",
				"en": " Trainer "
			},
			"1626": {
				"cn": " 培训策划 ",
				"en": " Training Planning "
			},
			"1627": {
				"cn": " 培训助理 ",
				"en": " Training Assistant "
			},
			"1628": {
				"cn": " 培训/课程顾问 ",
				"en": " Training/Course Consultant "
			},
			"1629": {
				"cn": " 培训产品开发 ",
				"en": " Training Product Development "
			},
			"1630": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1044": {
			"1631": {
				"cn": " 科研人员 ",
				"en": " Research Specialist Staff "
			},
			"1632": {
				"cn": " 科研管理人员 ",
				"en": " Research Management "
			}
		}
	},
	"1010": {
		"1045": {
			"1633": {
				"cn": " 餐饮/娱乐管理 ",
				"en": " Restaurant & Food / Entertainment Services Management "
			},
			"1634": {
				"cn": " 餐饮/娱乐领班/部长 ",
				"en": " Restaurant & Food / Entertainment Services Supervisor "
			},
			"1635": {
				"cn": " 餐饮/娱乐服务员 ",
				"en": " Restaurant & Food / Entertainment Services Waiter "
			},
			"1636": {
				"cn": " 礼仪/迎宾 ",
				"en": " Reception "
			},
			"1637": {
				"cn": " 司仪 ",
				"en": " Event Host "
			},
			"1638": {
				"cn": " 行政主厨/厨师长 ",
				"en": " Executive Chef "
			},
			"1639": {
				"cn": " 厨师/面点师 ",
				"en": " Chef/Cook "
			},
			"1640": {
				"cn": " 调酒师/侍酒师/吧台员 ",
				"en": " Bartender/Sommelier "
			},
			"1641": {
				"cn": " 茶艺师 ",
				"en": " Tea Specialist "
			},
			"1642": {
				"cn": " 传菜主管/传菜员 ",
				"en": " Food Server "
			},
			"1643": {
				"cn": " 厨师助理/学徒 ",
				"en": " Cooking Assistant "
			},
			"1644": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1046": {
			"1645": {
				"cn": " 酒店/宾馆经理 ",
				"en": " Hotel Manager "
			},
			"1646": {
				"cn": " 酒店/宾馆营销 ",
				"en": " Hotel Sales "
			},
			"1647": {
				"cn": " 大堂经理 ",
				"en": " Hall Manager "
			},
			"1648": {
				"cn": " 楼面经理 ",
				"en": " Floor Manager "
			},
			"1649": {
				"cn": " 前厅接待 ",
				"en": " Reception "
			},
			"1650": {
				"cn": " 客房服务员/楼面服务员 ",
				"en": " Room Service "
			},
			"1651": {
				"cn": " 行李员 ",
				"en": " Bellperson "
			},
			"1652": {
				"cn": " 清洁服务人员 ",
				"en": " Housekeeping Staff "
			},
			"1653": {
				"cn": " 导游/旅行顾问 ",
				"en": " Tour Guide/Travel Consultant "
			},
			"1654": {
				"cn": " 票务/订房服务 ",
				"en": " Reservation Service "
			},
			"1655": {
				"cn": " 宴会管理 ",
				"en": " Banquet Management "
			},
			"1656": {
				"cn": " 机场代表 ",
				"en": " Hotel Airport Representatives "
			},
			"1657": {
				"cn": " 管家部经理/主管 ",
				"en": " Housekeeping Manager "
			},
			"1658": {
				"cn": " 宾客服务经理 ",
				"en": " Guest Service Manager "
			},
			"1659": {
				"cn": " 预定部主管 ",
				"en": " Reservation Supervisor "
			},
			"1660": {
				"cn": " 预定员 ",
				"en": " Reservation Staff "
			},
			"1661": {
				"cn": " 健身房服务 ",
				"en": " Fitness Center Service "
			},
			"1662": {
				"cn": " 旅游产品销售 ",
				"en": " Tourism Product Sales "
			},
			"1663": {
				"cn": " 行程管理/计调 ",
				"en": " Travel Management "
			},
			"1664": {
				"cn": " 签证专员 ",
				"en": " Visa Specialist "
			},
			"1665": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1047": {
			"1666": {
				"cn": " 美容顾问/化妆 ",
				"en": " Beauty Advisor/Makeup "
			},
			"1667": {
				"cn": " 美容助理/见席美容师 ",
				"en": " Beautician Assistant "
			},
			"1668": {
				"cn": " 瘦身顾问 ",
				"en": " Slimming/Weight Loss Conunselor "
			},
			"1669": {
				"cn": " 发型师 ",
				"en": " Hair Stylist "
			},
			"1670": {
				"cn": " 发型助理/学徒 ",
				"en": " Hair Stylist Assistant "
			},
			"1671": {
				"cn": " 美甲师 ",
				"en": " Nail Specialist "
			},
			"1672": {
				"cn": " 按摩/足疗 ",
				"en": " Spa/Massage/Foot Care "
			},
			"1673": {
				"cn": " 健身顾问/教练 ",
				"en": " Fitness Trainer "
			},
			"1674": {
				"cn": " 瑜伽/舞蹈老师 ",
				"en": " Yoga/Dance Instructor "
			},
			"1675": {
				"cn": " 宠物护理/美容 ",
				"en": " Pet Care "
			},
			"1676": {
				"cn": " 体育运动教练 ",
				"en": " Coach "
			},
			"1677": {
				"cn": " 彩妆培训师 ",
				"en": " Makeup Trainer "
			},
			"1678": {
				"cn": " 专柜彩妆顾问(BA) ",
				"en": " Beauty Advisor "
			},
			"1679": {
				"cn": " 救生员 ",
				"en": " Lifeguard "
			},
			"1680": {
				"cn": " 美容导师 ",
				"en": " Beauty Supervisor "
			},
			"1681": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1048": {
			"1682": {
				"cn": " 店长/卖场经理/楼面管理 ",
				"en": " Store Manager/Floor Manager "
			},
			"1683": {
				"cn": " 店员/营业员 ",
				"en": " Store Manager Trainee/Salesperson "
			},
			"1684": {
				"cn": " 收银主管/收银员 ",
				"en": " Cashier "
			},
			"1685": {
				"cn": " 理货员/陈列员/收货员 ",
				"en": " Inventory Management/Display/Receiver "
			},
			"1686": {
				"cn": " 导购员 ",
				"en": " Sales "
			},
			"1687": {
				"cn": " 兼职店员 ",
				"en": " Part-time Salesperson "
			},
			"1688": {
				"cn": " 防损员/内保 ",
				"en": " Loss Prevention "
			},
			"1689": {
				"cn": " 西点师/面包糕点加工 ",
				"en": " Pastry/Bakery Assistant "
			},
			"1690": {
				"cn": " 熟食加工 ",
				"en": " Raw Food Assistant "
			},
			"1691": {
				"cn": " 品类经理 ",
				"en": " Cooked Food Assistant "
			},
			"1692": {
				"cn": " 安防主管 ",
				"en": " Category Manager "
			},
			"1693": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1049": {
			"1694": {
				"cn": " 乘务员 ",
				"en": " Attendant "
			},
			"1695": {
				"cn": " 司机 ",
				"en": " Chauffeur/Driver "
			},
			"1696": {
				"cn": " 飞机机长/副机长 ",
				"en": " Flight Captain "
			},
			"1697": {
				"cn": " 空乘人员 ",
				"en": " Flight Attendant "
			},
			"1698": {
				"cn": " 地勤人员 ",
				"en": " Ground Attendant "
			},
			"1699": {
				"cn": " 列车/地铁车长 ",
				"en": " Train/Subway Conductor "
			},
			"1700": {
				"cn": " 列车/地铁司机 ",
				"en": " Train/Subway Driver "
			},
			"1701": {
				"cn": " 船长/副船长 ",
				"en": " Fleet Captain "
			},
			"1702": {
				"cn": " 船员 ",
				"en": " Sailor "
			},
			"1703": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1050": {
			"1704": {
				"cn": " 保安人员 ",
				"en": " Security "
			},
			"1705": {
				"cn": " 保镖 ",
				"en": " Bodyguard "
			},
			"1706": {
				"cn": " 寻呼员/话务员 ",
				"en": " Paging Operator "
			},
			"1707": {
				"cn": " 搬运工 ",
				"en": " Mover "
			},
			"1708": {
				"cn": " 清洁工 ",
				"en": " Cleaning Staff "
			},
			"1709": {
				"cn": " 家政服务/保姆 ",
				"en": " Housekeeping/Nanny "
			},
			"1710": {
				"cn": " 保安经理 ",
				"en": " Security Manager "
			},
			"1711": {
				"cn": " 其他 ",
				"en": " Others "
			}
		}
	},
	"1011": {
		"1051": {
			"1712": {
				"cn": " 公务员 ",
				"en": " Official "
			}
		},
		"1052": {
			"1713": {
				"cn": " 英语翻译 ",
				"en": " English Translator "
			},
			"1714": {
				"cn": " 日语翻译 ",
				"en": " Japanese Translator "
			},
			"1715": {
				"cn": " 德语翻译 ",
				"en": " German Translator "
			},
			"1716": {
				"cn": " 法语翻译 ",
				"en": " French Translator "
			},
			"1717": {
				"cn": " 俄语翻译 ",
				"en": " Russian Translator "
			},
			"1718": {
				"cn": " 西班牙语翻译 ",
				"en": " Spanish Translator "
			},
			"1719": {
				"cn": " 韩语/朝鲜语翻译 ",
				"en": " Korean Translator "
			},
			"1720": {
				"cn": " 阿拉伯语翻译 ",
				"en": " Arabic Translator "
			},
			"1721": {
				"cn": " 意大利语翻译 ",
				"en": " Italian Translator "
			},
			"1722": {
				"cn": " 葡萄牙语翻译 ",
				"en": " Portuguese Translator "
			},
			"1723": {
				"cn": " 泰语翻译 ",
				"en": " Thai Translator "
			},
			"1724": {
				"cn": " 中国方言翻译 ",
				"en": " Chinese Dialect Translator "
			},
			"1725": {
				"cn": " 其他语种翻译 ",
				"en": " Other Language Translator "
			}
		},
		"1053": {
			"1726": {
				"cn": " 中专/职校生 ",
				"en": " Technical/Vocational School Student "
			},
			"1727": {
				"cn": " 大学/大专应届毕业生 ",
				"en": " University/College Graduating Student "
			},
			"1728": {
				"cn": " 研究生 ",
				"en": " Graduate Student "
			},
			"1729": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1054": {
			"1730": {
				"cn": " 培训生 ",
				"en": " Trainee "
			},
			"1731": {
				"cn": " 储备干部 ",
				"en": " Associate Trainee "
			},
			"1732": {
				"cn": " 实习生 ",
				"en": " Intern "
			}
		},
		"1055": {
			"1733": {
				"cn": " 兼职 ",
				"en": " Part Time "
			}
		},
		"1056": {
			"1737": {
				"cn": " 环保工程师 ",
				"en": " Environmental Protection Engineer "
			},
			"1738": {
				"cn": " 水处理工程师 ",
				"en": " Water Treatment Engineer "
			},
			"1739": {
				"cn": " 环境影响评价工程师 ",
				"en": " Environmental Impact Assessment Engineer "
			},
			"1740": {
				"cn": " 环保检测 ",
				"en": " Environmental Inspector "
			},
			"1741": {
				"cn": " 水质检测员 ",
				"en": " Water Quality Inspector "
			},
			"1742": {
				"cn": " 固废工程师 ",
				"en": " Waste Treatment Engineer "
			},
			"1743": {
				"cn": " 废气处理工程师 ",
				"en": " Waste Gas Treatment Engineer "
			},
			"1744": {
				"cn": " 其它 ",
				"en": " Others "
			}
		},
		"1057": {
			"1745": {
				"cn": " 养殖部主管 ",
				"en": " Culturist "
			},
			"1746": {
				"cn": " 场长(农/林/牧/渔业) ",
				"en": " Director(Agriculture/Forestry/Fishing) "
			},
			"1747": {
				"cn": " 农艺师 ",
				"en": " Agronomist "
			},
			"1748": {
				"cn": " 畜牧师 ",
				"en": " Animal Husbandry "
			},
			"1749": {
				"cn": " 饲养员 ",
				"en": " Animal Care Technician "
			},
			"1750": {
				"cn": " 动物营养/饲料研发 ",
				"en": " Animal Food R&D "
			},
			"1751": {
				"cn": " 其他 ",
				"en": " Others "
			}
		},
		"1058": {
			"1734": {
				"cn": " 驯兽师/助理驯兽师 ",
				"en": " Animal Trainer "
			},
			"1735": {
				"cn": " 志愿者/社会工作者 ",
				"en": " Volunteer /Social Worker "
			},
			"1736": {
				"cn": " 其他 ",
				"en": " Others "
			}
		}
	}

}
