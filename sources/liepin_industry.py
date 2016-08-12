# encoding: utf-8

industry_list = {
	'150' : u'保险',
	'620' : u'IT管理/项目协调',
	'210' : u'生产/营运',
	'090' : u'财务/审计/税务',
	'310' : u'实习生/培训生/储备干部',
	'191' : u'酒店/餐饮/娱乐/生活服务',
	'190' : u'旅游/出入境服务',
	'010' : u'高级管理',
	'390' : u'硬件开发',
	'110' : u'电信/通信技术开发及应用',
	'250' : u'写作/采编/出版/印刷',
	'050' : u'质量管理/安全防护',
	'040' : u'项目管理/项目协调',
	'170' : u'建筑装潢/市政建设',
	'070' : u'人力资源',
	'490' : u'化工',
	'470' : u'广告/会展',
	'450' : u'采购/贸易',
	'180' : u'翻译',
	'500' : u'环境科学/环保',
	'520' : u'物业管理',
	'340' : u'其他',
	'650' : u'房地产交易/中介',
	'400' : u'电子/电器/半导体/仪器/仪表',
	'420' : u'汽车制造',
	'480' : u'影视/媒体',
	'360' : u'产品/运营/设计',
	'320' : u'农/林/牧/渔',
	'630' : u'IT运维/技术支持',
	'060' : u'市场',
	'080' : u'行政/后勤/文秘',
	'140' : u'基金/证券/期货/投资',
	'300' : u'公务员/事业单位/科研',
	'563' : u'信托/担保/拍卖/典当',
	'440' : u'服装/纺织/皮革',
	'460' : u'公关/媒介',
	'120' : u'电力/能源/矿产/地质勘查',
	'260' : u'教育/培训',
	'240' : u'艺术/设计',
	'280' : u'医院/医疗/护理',
	'100' : u'IT质量管理/测试/配置管理',
	'160' : u'物流/仓储',
	'220' : u'机械设计/制造/维修',
	'270' : u'律师/法务/合规',
	'537' : u'销售行政/商务',
	'536' : u'销售人员',
	'535' : u'销售管理',
	'130' : u'咨询/调研',
	'410' : u'银行',
	'290' : u'生物/制药/医疗器械',
	'350' : u'软件/互联网开发/系统集成',
	'510' : u'房地产规划/开发',
	'291' : u'百货/连锁/零售服务',
	'292' : u'交通运输服务',
	'430' : u'汽车销售与服务',
	'538' : u'客户服务/技术支持'
}

job_list = {
	'150' : {
		'150030' : {
			'cn' :u'保险培训师',
			'en' :'Insurance Trainer'
			},
		'150020' : {
			'cn' :u'核保/理赔',
			'en' :'Underwriting/Claim Management'
			},
		'150090' : {
			'cn' :u'产品开发/项目策划',
			'en' :'Product Development/Planner'
			},
		'150100' : {
			'cn' :u'保险顾问/财务规划师',
			'en' :' Insurance Consultant'
			},
		'150110' : {
			'cn' :u'保险内勤',
			'en' :'Staff'
			},
		'150010' : {
			'cn' :u'稽核/法律/合规',
			'en' :'Compliance/Audit'
			},
		'150050' : {
			'cn' :u'客户服务/续期管理',
			'en' :'Customer Service/Account Renewals Management'
			},
		'150040' : {
			'cn' :u'保险代理人/经纪人/客户经理',
			'en' :'Insurance Agent/Broker/Account Manager'
			},
		'150131' : {
			'cn' :u'再保险',
			'en' :'Reinsurance'
			},
		'150132' : {
			'cn' :u'行业研究',
			'en' :'Industry Research'
			},
		'150070' : {
			'cn' :u'保险精算师',
			'en' :'Actuary'
			},
		'150080' : {
			'cn' :u'业务经理/主管',
			'en' :'Business Manager/Supervisor'
			},
		'150130' : {
			'cn' :u'契约管理',
			'en' :'Policy Management'
			},
		'150060' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'150120' : {
			'cn' :u'储备经理人',
			'en' :'Agency Management Associate'
			},
	},
	'620' : {
		'360339' : {
			'cn' :u'技术/研发经理',
			'en' :'Technology Manager'
			},
		'100060' : {
			'cn' :u'项目经理/主管',
			'en' :'Project Manager/Supervisor'
			},
		'100070' : {
			'cn' :u'项目执行/协调人员',
			'en' :'Project Specialist/Coordinator'
			},
		'100370' : {
			'cn' :u'项目总监',
			'en' :'Project Director'
			},
		'010030' : {
			'cn' :u'首席技术官CTO/首席信息官CIO',
			'en' :'Chief Technology Officer/Chief Information Officer'
			},
		'620010' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'100170' : {
			'cn' :u'工程与项目实施',
			'en' :'Engineering and Project Implementation'
			},
		'100020' : {
			'cn' :u'技术/研发总监',
			'en' :'Technology Director'
			},
	},
	'210' : {
		'160210' : {
			'cn' :u'供应链总监',
			'en' :'Supply Chain Director'
			},
		'160095' : {
			'cn' :u'供应链经理/主管',
			'en' :'Supply Chain Executive/Manager/Director'
			},
		'210110' : {
			'cn' :u'生产质量管理',
			'en' :'Production Quality Management'
			},
		'210170' : {
			'cn' :u'工艺/制程工程师(PE)',
			'en' :'PE Engineer'
			},
		'210015' : {
			'cn' :u'运营经理/主管',
			'en' :'Operations Manager/Supervisor'
			},
		'210150' : {
			'cn' :u'组长/拉长',
			'en' :'Group Leader'
			},
		'210030' : {
			'cn' :u'生产项目工程师',
			'en' :'Production Project Engineer'
			},
		'210210' : {
			'cn' :u'工厂经理/厂长',
			'en' :'Plant/Factory Manager'
			},
		'210070' : {
			'cn' :u'安全/健康/环境管理',
			'en' :'Safety/Health/Environmental Management'
			},
		'210130' : {
			'cn' :u'维修工程师',
			'en' :'Maintenance Engineer'
			},
		'210050' : {
			'cn' :u'生产物料管理(PMC)',
			'en' :'Production Material Control(PMC)'
			},
		'210250' : {
			'cn' :u'包装工程师',
			'en' :'Packaging Engineer'
			},
		'210270' : {
			'cn' :u'维修经理/主管',
			'en' :'Maintenance Manager/Supervisor'
			},
		'210230' : {
			'cn' :u'生产项目经理/主管',
			'en' :'Production Project Manager/Supervisor'
			},
		'210190' : {
			'cn' :u'制造工程师',
			'en' :'Manufacturing Engineer'
			},
		'160220' : {
			'cn' :u'供应链专员/助理',
			'en' :'Supply Chain Specialist/Assistant'
			},
		'210160' : {
			'cn' :u'生产计划/调度',
			'en' :'Production Planning/Scheduling'
			},
		'210060' : {
			'cn' :u'生产设备管理',
			'en' :'Production Equipment Management'
			},
		'210020' : {
			'cn' :u'总工程师/副总工程师',
			'en' :'Chief Engineer/Deputy Chief Engineer'
			},
		'210140' : {
			'cn' :u'生产经理/车间主任',
			'en' :'Production Manager/Workshop Supervisor'
			},
		'210090' : {
			'cn' :u'技术或工艺设计经理',
			'en' :'Technology or Process Design Manager'
			},
		'210200' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'210040' : {
			'cn' :u'采购管理',
			'en' :'Purchasing Management'
			},
		'210120' : {
			'cn' :u'仓库管理',
			'en' :'Warehouse Management'
			},
		'210180' : {
			'cn' :u'工业工程师(IE)',
			'en' :'Industrial Engineer'
			},
		'210220' : {
			'cn' :u'生产项目总监',
			'en' :'Production Project Director'
			},
		'210260' : {
			'cn' :u'生产文员',
			'en' :'Production Clerk'
			},
		'210080' : {
			'cn' :u'产品管理',
			'en' :'Product Management'
			},
		'210240' : {
			'cn' :u'生产总监',
			'en' :'Production Director'
			},
	},
	'090' : {
		'090180' : {
			'cn' :u'投融资经理/主管',
			'en' :'Investment and Finance Manager/Supervisor'
			},
		'090170' : {
			'cn' :u'税务专员/助理',
			'en' :'Tax Executive/Assistant'
			},
		'090050' : {
			'cn' :u'会计经理/主管',
			'en' :'Accounting Manager/Supervisor'
			},
		'090090' : {
			'cn' :u'财务分析员',
			'en' :'Financial Analyst'
			},
		'090190' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'090110' : {
			'cn' :u'成本管理员',
			'en' :'Capital Manager'
			},
		'090030' : {
			'cn' :u'财务经理',
			'en' :'Financial Manager'
			},
		'090150' : {
			'cn' :u'统计员',
			'en' :'Statistician'
			},
		'090130' : {
			'cn' :u'审计专员/助理',
			'en' :'Audit Executive/Assistant'
			},
		'090080' : {
			'cn' :u'财务分析经理/主管',
			'en' :'Financial Analysis Manager/Supervisor'
			},
		'090040' : {
			'cn' :u'财务主管/总帐主管',
			'en' :'Financial Director/General Accounts Director'
			},
		'090160' : {
			'cn' :u'税务经理/主管',
			'en' :'Tax Manager/Supervisor'
			},
		'090201' : {
			'cn' :u'会计助理/文员',
			'en' :'Accounting Clerk'
			},
		'090200' : {
			'cn' :u'财务顾问',
			'en' :'Finance Consultant'
			},
		'090203' : {
			'cn' :u'资产/资金管理',
			'en' :'Treasury Manager/Supervisor'
			},
		'090202' : {
			'cn' :u'出纳员',
			'en' :'Cashier'
			},
		'090120' : {
			'cn' :u'审计经理/主管',
			'en' :'Audit Manager/Supervisor'
			},
		'090020' : {
			'cn' :u'财务总监',
			'en' :'Chief Financial Officer'
			},
		'090100' : {
			'cn' :u'成本经理/主管',
			'en' :'Cost Accounting Manager/Supervisor'
			},
		'090060' : {
			'cn' :u'会计/会计师',
			'en' :'Accountant'
			},
		'090140' : {
			'cn' :u'财务助理',
			'en' :'Finance Assistant'
			},
		'010040' : {
			'cn' :u'首席财务官CFO',
			'en' :'Chief Financial Officer/CFO'
			},
	},
	'310' : {
		'310020' : {
			'cn' :u'实习生',
			'en' :'Intern'
			},
		'310050' : {
			'cn' :u'储备干部',
			'en' :'Associate Trainee'
			},
		'310040' : {
			'cn' :u'培训生',
			'en' :'Trainee'
			},
		'310060' : {
			'cn' :u'其他',
			'en' :'Others'
			},
	},
	'191' : {
		'190030' : {
			'cn' :u'大堂经理/领班',
			'en' :'Lobby Manager/Supervisor'
			},
		'190020' : {
			'cn' :u'餐饮/娱乐管理',
			'en' :'Restaurant & Food / Entertainment Services Management'
			},
		'190170' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'190100' : {
			'cn' :u'导游/旅行顾问',
			'en' :'Tour Guide/Travel Consultant'
			},
		'190230' : {
			'cn' :u'宾客服务经理',
			'en' :'Guest Service Manager'
			},
		'190010' : {
			'cn' :u'酒店/宾馆管理',
			'en' :'Hotel Management'
			},
		'190050' : {
			'cn' :u'厨师/调酒师/茶艺师',
			'en' :'Chef/Bartender/Tea Service'
			},
		'190240' : {
			'cn' :u'预定部主管',
			'en' :'Reservation Supervisor'
			},
		'190180' : {
			'cn' :u'酒店/宾馆营销',
			'en' :'Hotel Sales'
			},
		'190250' : {
			'cn' :u'预定员',
			'en' :'Reservation Staff'
			},
		'190220' : {
			'cn' :u'管家部经理/主管',
			'en' :'Housekeeping Manager'
			},
		'190060' : {
			'cn' :u'营养师',
			'en' :'Dietitian'
			},
		'190110' : {
			'cn' :u'健身教练',
			'en' :'Fitness Coach'
			},
		'190040' : {
			'cn' :u'楼面管理',
			'en' :'Floor Management'
			},
		'470011' : {
			'cn' :u'婚礼策划服务',
			'en' :'Wedding Planning Service'
			},
		'190200' : {
			'cn' :u'宴会管理',
			'en' :'Banquet Management'
			},
		'190120' : {
			'cn' :u'美容美发',
			'en' :'Beauty Salon'
			},
	},
	'190' : {
		'190280' : {
			'cn' :u'签证专员',
			'en' :'Visa Specialist'
			},
		'190270' : {
			'cn' :u'行程管理/计调',
			'en' :'Travel Management'
			},
		'190260' : {
			'cn' :u'旅游产品销售',
			'en' :'Tourism Product Sales'
			},
		'190190' : {
			'cn' :u'票务服务',
			'en' :'Ticket Service'
			},
		'191020' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'190210' : {
			'cn' :u'机场代表',
			'en' :'Hotel Airport Representatives'
			},
	},
	'010' : {
		'010010' : {
			'cn' :u'首席执行官CEO/总裁/总经理',
			'en' :'CEO/President/General Manager'
			},
		'010102' : {
			'cn' :u'分公司/代表处负责人',
			'en' :'Head of Branch Company'
			},
		'010020' : {
			'cn' :u'首席运营官COO',
			'en' :'Chief Operating Officer/COO'
			},
		'010101' : {
			'cn' :u'投资者关系',
			'en' :'Investor Relations'
			},
		'010060' : {
			'cn' :u'合伙人',
			'en' :'Partner'
			},
		'010070' : {
			'cn' :u'部门/事业部管理',
			'en' :'Department Management'
			},
		'010103' : {
			'cn' :u'企业秘书/董事会秘书',
			'en' :'Corporate/Board Secretary'
			},
		'010130' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'010050' : {
			'cn' :u'副总裁/副总经理',
			'en' :'Vice President/Deputy General Manager'
			},
		'010080' : {
			'cn' :u'总裁助理/总经理助理',
			'en' :'Executive Assistant/General Manager Assistant'
			},
	},
	'390' : {
		'100130' : {
			'cn' :u'高级硬件工程师',
			'en' :'Senior Hardware Engineer'
			},
		'110065' : {
			'cn' :u'嵌入式硬件开发(主板机…)',
			'en' :'Embedded Hardware Engineer(PCB…)'
			},
		'390002' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'100150' : {
			'cn' :u'硬件工程师',
			'en' :'Hardware Engineer'
			},
	},
	'110' : {
		'110270' : {
			'cn' :u'通信电源工程师',
			'en' :'Communication Power Supply Engineer'
			},
		'110260' : {
			'cn' :u'电信网络工程师',
			'en' :'Telecommunication Network Engineer'
			},
		'110290' : {
			'cn' :u'通信项目管理',
			'en' :'Communication Project Management'
			},
		'110280' : {
			'cn' :u'增值产品开发工程师',
			'en' :'Value-Added Product Development Engineer'
			},
		'110220' : {
			'cn' :u'有线传输工程师',
			'en' :'Wired Transmission Engineer'
			},
		'110210' : {
			'cn' :u'通信技术工程师',
			'en' :'Communication Engineer'
			},
		'110200' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'110250' : {
			'cn' :u'移动通信工程师',
			'en' :'Mobile Communication Engineer'
			},
		'110030' : {
			'cn' :u'电信/通讯工程师',
			'en' :'Telecommunications/Communications Engineer'
			},
		'110240' : {
			'cn' :u'数据通信工程师',
			'en' :'Data Communication Engineer'
			},
		'110300' : {
			'cn' :u'通信标准化工程师',
			'en' :'Communication Standardization Engineer'
			},
		'110080' : {
			'cn' :u'无线/射频通信工程师',
			'en' :'RF/ Communication Engineer'
			},
		'110230' : {
			'cn' :u'电信交换工程师',
			'en' :'Telecommunication Exchange Engineer'
			},
	},
	'250' : {
		'250070' : {
			'cn' :u'校对/录入',
			'en' :'Proofreading/Copy Entry'
			},
		'250200' : {
			'cn' :u'电分操作员',
			'en' :'Operator-Colour Distinguishing'
			},
		'250240' : {
			'cn' :u'印刷机械机长',
			'en' :'Printing Machine Operator'
			},
		'250250' : {
			'cn' :u'记者/采编',
			'en' :'Reporter'
			},
		'250080' : {
			'cn' :u'排版设计',
			'en' :'Layout Design'
			},
		'250030' : {
			'cn' :u'文字编辑/组稿',
			'en' :'Copy Editor'
			},
		'250190' : {
			'cn' :u'电话采编',
			'en' :'Telephone Reporter'
			},
		'250180' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'250010' : {
			'cn' :u'作家/编剧/撰稿人',
			'en' :'Writer/Screenwriter'
			},
		'250210' : {
			'cn' :u'印刷排版/制版',
			'en' :'Layout Designer'
			},
		'250040' : {
			'cn' :u'美术编辑',
			'en' :'Art Editor'
			},
		'250050' : {
			'cn' :u'发行管理',
			'en' :'Distribution Management'
			},
		'220180' : {
			'cn' :u'包装/印刷',
			'en' :'Packaging/Printing'
			},
		'250220' : {
			'cn' :u'数码直印/菲林输出',
			'en' :'Digital/Film Printing'
			},
		'250230' : {
			'cn' :u'调墨技师',
			'en' :'Ink Technician'
			},
		'250020' : {
			'cn' :u'总编/副总编',
			'en' :'General Editor/Deputy Editor'
			},
	},
	'050' : {
		'050050' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'050060' : {
			'cn' :u'环境/健康/安全(EHS)经理/主管',
			'en' :'EHS Manager/Supervisor'
			},
		'050070' : {
			'cn' :u'认证工程师/审核员',
			'en' :'Certification Engineer/Auditor'
			},
		'050020' : {
			'cn' :u'质量管理/测试主管(QA/QC主管)',
			'en' :'QA/QC Supervisor'
			},
		'050030' : {
			'cn' :u'质量检测员/测试员',
			'en' :'Quality Inspector/Tester'
			},
		'050080' : {
			'cn' :u'体系工程师/审核员',
			'en' :'Systems Engineer/Auditor'
			},
		'050090' : {
			'cn' :u'可靠度工程师',
			'en' :'Reliability Engineer'
			},
		'050040' : {
			'cn' :u'供应商/采购质量管理',
			'en' :'Supplier/Purchasing Quality Management'
			},
		'340020' : {
			'cn' :u'安全防护/安全管理',
			'en' :'Safety Protection'
			},
		'050010' : {
			'cn' :u'质量管理/测试经理(QA/QC经理)',
			'en' :'QA/QC Manager'
			},
		'050110' : {
			'cn' :u'环境/健康/安全(EHS)工程师',
			'en' :'EHS Engineer'
			},
		'050100' : {
			'cn' :u'故障分析工程师',
			'en' :'Failure Analysis Engineer'
			},
	},
	'040' : {
		'040010' : {
			'cn' :u'项目总监',
			'en' :'Project Director'
			},
		'040030' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'040020' : {
			'cn' :u'项目经理/主管',
			'en' :'Project Manager/Supervisor'
			},
		'040040' : {
			'cn' :u'项目专员/助理',
			'en' :'Project Specialist/Assistant'
			},
	},
	'170' : {
		'170203' : {
			'cn' :u'资料员',
			'en' :'Data Management Specialist'
			},
		'170010' : {
			'cn' :u'建筑工程师',
			'en' :'Architect'
			},
		'170130' : {
			'cn' :u'室内装潢设计',
			'en' :'Interior Design'
			},
		'170201' : {
			'cn' :u'建筑工程安全管理',
			'en' :'Construction Security Management'
			},
		'170030' : {
			'cn' :u'建筑设计师',
			'en' :'Architectural Designer'
			},
		'170110' : {
			'cn' :u'道路/桥梁/隧道工程技术',
			'en' :'Road/Bridge/Tunnel Technology'
			},
		'170202' : {
			'cn' :u'智能大厦/综合布线/安防/弱电',
			'en' :'Intelligent Building/Integrated Wiring/Defence&Security/Weak Current'
			},
		'170194' : {
			'cn' :u'楼宇自动化',
			'en' :'Building Automation'
			},
		'170195' : {
			'cn' :u'建筑机电工程师',
			'en' :'Building Electrical Engineer'
			},
		'170196' : {
			'cn' :u'幕墙工程师',
			'en' :'Curtain Wall Engineer'
			},
		'170197' : {
			'cn' :u'建筑制图/模型/渲染',
			'en' :'CAD Drafter/Building Model/Rendering'
			},
		'170190' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'170191' : {
			'cn' :u'高级建筑工程师/总工',
			'en' :'Senior Architect'
			},
		'170206' : {
			'cn' :u'钢结构工程师',
			'en' :'Steel Structure Engineer'
			},
		'170193' : {
			'cn' :u'岩土工程',
			'en' :'Geotechnical Engineer'
			},
		'170208' : {
			'cn' :u'空调工程师',
			'en' :'Air Conditioner Engineer'
			},
		'170209' : {
			'cn' :u'安装造价工程师',
			'en' :'Installation Cost Engineer'
			},
		'170199' : {
			'cn' :u'市政工程师',
			'en' :'Municipal Project Engineer'
			},
		'170170' : {
			'cn' :u'公路桥梁预算师',
			'en' :'Road and Bridge Estimator'
			},
		'170205' : {
			'cn' :u'现场/施工管理',
			'en' :'Construction Management'
			},
		'170192' : {
			'cn' :u'建筑工程验收',
			'en' :'Construction Project Inspector'
			},
		'170090' : {
			'cn' :u'建筑设备工程师',
			'en' :'Construction Equipment Engineer'
			},
		'170207' : {
			'cn' :u'爆破工程师',
			'en' :'Blast Engineer'
			},
		'170200' : {
			'cn' :u'合同管理',
			'en' :'Contract Management'
			},
		'170150' : {
			'cn' :u'城市规划与设计',
			'en' :'Urban Planning and Design'
			},
		'340040' : {
			'cn' :u'测绘/测量',
			'en' :'Mapping/Surveyor'
			},
		'170120' : {
			'cn' :u'园艺/园林/景观设计',
			'en' :'Gardenning Designer'
			},
		'170100' : {
			'cn' :u'工程预结算管理',
			'en' :'Construction Budget/Cost Management'
			},
		'170020' : {
			'cn' :u'土木/土建工程师',
			'en' :'Civil Engineer'
			},
		'170050' : {
			'cn' :u'工程监理',
			'en' :'Project Management'
			},
		'170180' : {
			'cn' :u'施工员',
			'en' :'Construction Worker'
			},
		'170040' : {
			'cn' :u'建筑工程管理/项目经理',
			'en' :'Construction Management'
			},
		'170060' : {
			'cn' :u'给排水/制冷暖通',
			'en' :'Drainage / refrigeration HVAC'
			},
		'170214' : {
			'cn' :u'架线和管道工程技术',
			'en' :'Pipeline Engineering Technology'
			},
		'170213' : {
			'cn' :u'软装设计师',
			'en' :'Soft outfit Designer'
			},
		'170212' : {
			'cn' :u'水利/港口工程技术',
			'en' :'Water Conservancy/Port Engineering Technology'
			},
		'170211' : {
			'cn' :u'结构工程师',
			'en' :'Structural Engineer'
			},
		'170210' : {
			'cn' :u'土建造价工程师',
			'en' :'Civil Engineering Cost Engineer '
			},
	},
	'070' : {
		'070121' : {
			'cn' :u'绩效专员/助理',
			'en' :'Performance Assessment Specialist/Assistant'
			},
		'070070' : {
			'cn' :u'培训经理/主管',
			'en' :'Training Manager/Supervisor'
			},
		'010121' : {
			'cn' :u'首席人力资源官CHO/HRVP',
			'en' :'Chief Human Resource Officer/Vice President'
			},
		'070160' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'070040' : {
			'cn' :u'人力资源专员/助理',
			'en' :'HR Specialist/Assistant'
			},
		'070050' : {
			'cn' :u'招聘经理/主管',
			'en' :'Recruiting Manager/Supervisor'
			},
		'070051' : {
			'cn' :u'招聘专员/助理',
			'en' :'Recruiting Specialist/Assistant'
			},
		'070162' : {
			'cn' :u'猎头顾问/助理',
			'en' :'Headhunter/Assistant'
			},
		'070100' : {
			'cn' :u'薪资福利经理/主管',
			'en' :'Compensation and Benefits Manager/Director'
			},
		'070010' : {
			'cn' :u'人力资源总监',
			'en' :'Director of Human Resources'
			},
		'070161' : {
			'cn' :u'企业培训师/讲师',
			'en' :'Staff Trainer'
			},
		'070120' : {
			'cn' :u'绩效经理/主管',
			'en' :'Performance Assessment Manager/Supervisor'
			},
		'070101' : {
			'cn' :u'薪资福利专员/助理',
			'en' :'Compensation & Benefits Specialist/Assistant'
			},
		'070080' : {
			'cn' :u'培训专员/助理',
			'en' :'Training Specialist/Assistant'
			},
		'070020' : {
			'cn' :u'人力资源经理/主管',
			'en' :'Human Resources Manager/Supervisor'
			},
		'070140' : {
			'cn' :u'员工关系/企业文化/工会',
			'en' :'Employee Relations/Corporate Culture/Unions'
			},
		'070141' : {
			'cn' :u'人力资源信息系统',
			'en' :'HRIS'
			},
		'070142' : {
			'cn' :u'人力资源伙伴(HRBP)',
			'en' :'HR Business Partner'
			},
		'070143' : {
			'cn' :u'组织发展(OD)',
			'en' :'Organization Development'
			},
	},
	'490' : {
		'490003' : {
			'cn' :u'配色技术员',
			'en' :'Color Matcher (Technician)'
			},
		'490002' : {
			'cn' :u'涂料研发工程师',
			'en' :'R&D Chemist Scientist'
			},
		'490001' : {
			'cn' :u'化工实验室研究员/技术员',
			'en' :'Chemical Lab Scientist / Technician'
			},
		'490007' : {
			'cn' :u'造纸研发',
			'en' :'Paper Making Scientist'
			},
		'490006' : {
			'cn' :u'食品/饮料研发',
			'en' :'Food / Beverage Scientist'
			},
		'490005' : {
			'cn' :u'化妆品研发',
			'en' :'Cosmetics Scientist'
			},
		'490004' : {
			'cn' :u'塑料工程师',
			'en' :'Plastics Engineer'
			},
		'490008' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'290060' : {
			'cn' :u'化工技术应用/化工工程师',
			'en' :'Chemical Technical Application/Chemical Engineer'
			},
	},
	'470' : {
		'060170' : {
			'cn' :u'广告客户经理/主管',
			'en' :'Advertising Account Manager/Supervisor'
			},
		'060150' : {
			'cn' :u'广告创意/设计经理/主管',
			'en' :'Advertising Creative Manager/Supervisor'
			},
		'470001' : {
			'cn' :u'广告客户总监',
			'en' :'Advertising Account Director'
			},
		'470010' : {
			'cn' :u'会展策划/设计',
			'en' :'Exhibition Planning /Design'
			},
		'470009' : {
			'cn' :u'会务/会展专员/助理',
			'en' :' Exhibition Specialist/Assistant'
			},
		'470008' : {
			'cn' :u'美术指导',
			'en' :'Art Director'
			},
		'060070' : {
			'cn' :u'会务/会展经理/主管',
			'en' :'Exhibition/Event Manager/Supervisor'
			},
		'470005' : {
			'cn' :u'文案/策划',
			'en' :'Copywriter/Planner'
			},
		'470004' : {
			'cn' :u'广告创意/设计师',
			'en' :'Advertising Designer'
			},
		'470014' : {
			'cn' :u'广告/会展项目管理',
			'en' :'Advertising/Exhibition Project Management'
			},
		'470006' : {
			'cn' :u'广告/会展业务拓展',
			'en' :'Advertising/Exhibition BD'
			},
		'470012' : {
			'cn' :u'制作执行',
			'en' :'Event executive'
			},
		'470013' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'470003' : {
			'cn' :u'广告创意/设计总监',
			'en' :'Advertising Creative Director'
			},
		'470002' : {
			'cn' :u'广告客户专员',
			'en' :'Advertising Account Executive'
			},
	},
	'450' : {
		'160070' : {
			'cn' :u'采购经理/主管',
			'en' :'Purchasing Executive/Manager/Director'
			},
		'160021' : {
			'cn' :u'商务经理/主管',
			'en' :'Business Manager/Supervisor'
			},
		'160020' : {
			'cn' :u'国内贸易经理/主管',
			'en' :'Domestic Trade manager/Supervisor'
			},
		'450010' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'160010' : {
			'cn' :u'外贸经理/主管',
			'en' :'Trading Manager/Supervisor'
			},
		'450009' : {
			'cn' :u'业务跟单员',
			'en' :'Merchandiser'
			},
		'450008' : {
			'cn' :u'业务跟单经理/主管',
			'en' :'Merchandising Manager/Supervisor'
			},
		'450007' : {
			'cn' :u'商务专员/助理',
			'en' :'Business Specialist/Assistant'
			},
		'450006' : {
			'cn' :u'国内贸易专员/助理',
			'en' :'Domestic Trade Specialist/Assistant'
			},
		'450005' : {
			'cn' :u'外贸专员/助理',
			'en' :'Trading Specialist/Assistant'
			},
		'450004' : {
			'cn' :u'供应商开发',
			'en' :'Supplier Development'
			},
		'450003' : {
			'cn' :u'买手',
			'en' :'Buyer'
			},
		'450002' : {
			'cn' :u'采购专员/助理',
			'en' :'Purchasing Specialist/Assistant'
			},
		'450001' : {
			'cn' :u'采购总监',
			'en' :'Purchasing Director'
			},
	},
	'180' : {
		'180040' : {
			'cn' :u'德语翻译',
			'en' :'German Translator'
			},
		'180050' : {
			'cn' :u'俄语翻译',
			'en' :'Russian Translator'
			},
		'180080' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'180020' : {
			'cn' :u'日语翻译',
			'en' :'Japanese Translator'
			},
		'180074' : {
			'cn' :u'泰语翻译',
			'en' :'Thai Translator'
			},
		'180075' : {
			'cn' :u'中国方言翻译',
			'en' :'Chinese Dialect Translator'
			},
		'180060' : {
			'cn' :u'西班牙语翻译',
			'en' :'Spanish Translator'
			},
		'180070' : {
			'cn' :u'韩语/朝鲜语翻译',
			'en' :'Korean Translator'
			},
		'180071' : {
			'cn' :u'阿拉伯语翻译',
			'en' :'Arabic Translator'
			},
		'180072' : {
			'cn' :u'意大利语翻译',
			'en' :'Italian Translator'
			},
		'180073' : {
			'cn' :u'葡萄牙语翻译',
			'en' :'Portuguese Translator'
			},
		'180030' : {
			'cn' :u'法语翻译',
			'en' :'French Translator'
			},
		'180010' : {
			'cn' :u'英语翻译',
			'en' :'English Translator'
			},
	},
	'500' : {
		'290070' : {
			'cn' :u'环保工程师',
			'en' :'Environmental Engineer'
			},
		'500008' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'500001' : {
			'cn' :u'水处理工程师',
			'en' :'Water Treatment Engineer'
			},
		'500003' : {
			'cn' :u'环保检测',
			'en' :'Environmental Inspector'
			},
		'500002' : {
			'cn' :u'环境评价工程师',
			'en' :'Environmental Assessment Engineer'
			},
		'500005' : {
			'cn' :u'固废处理工程师',
			'en' :'Solid Waste Treatment Engineer'
			},
		'500004' : {
			'cn' :u'水质检测员',
			'en' :'Water Quality Inspector'
			},
		'500007' : {
			'cn' :u'EHS管理',
			'en' :'EHS Management'
			},
		'500006' : {
			'cn' :u'废气处理工程师',
			'en' :'Waste Gas Treatment Engineer'
			},
	},
	'520' : {
		'170140' : {
			'cn' :u'物业管理经理/主管',
			'en' :'Property Management Manager/Supervisor'
			},
		'520003' : {
			'cn' :u'物业招商/租赁/租售',
			'en' :'Property Lease/Rent'
			},
		'520002' : {
			'cn' :u'高级物业顾问/物业顾问',
			'en' :'Senior Property Advisor/Property Advisor'
			},
		'520001' : {
			'cn' :u'物业管理专员/助理',
			'en' :'Property Management'
			},
		'520006' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'520005' : {
			'cn' :u'物业机电工程师',
			'en' :'Property Mechanical Engineer'
			},
		'520004' : {
			'cn' :u'物业设施管理人员',
			'en' :'Property Establishment Management'
			},
	},
	'340' : {
		'340080' : {
			'cn' :u'其他',
			'en' :'Others'
			},
	},
	'650' : {
		'510008' : {
			'cn' :u'房地产招商',
			'en' :'Real Estate Investment'
			},
		'170080' : {
			'cn' :u'房地产评估',
			'en' :'Real Estate Appraisal'
			},
		'510006' : {
			'cn' :u'房地产销售经理/主管',
			'en' :'Real Estate Sales Manager/Supervisor'
			},
		'510007' : {
			'cn' :u'房地产销售人员',
			'en' :'Real Estate Sales'
			},
		'170160' : {
			'cn' :u'房地产交易/中介',
			'en' :'Real Estate Agent/Broker'
			},
		'510018' : {
			'cn' :u'其他',
			'en' :'Others'
			},
	},
	'400' : {
		'110340' : {
			'cn' :u'激光/光电子技术',
			'en' :'Laser/Optoelectronics Technology'
			},
		'110190' : {
			'cn' :u'工程与项目实施',
			'en' :'Engineering and Project Implementation'
			},
		'110100' : {
			'cn' :u'电子元器件工程师',
			'en' :'Electronic Component Engineer'
			},
		'110040' : {
			'cn' :u'工艺/制程工程师(PE)',
			'en' :'PE Engineer'
			},
		'110403' : {
			'cn' :u'自动化工程师',
			'en' :'Automation Engineer'
			},
		'110320' : {
			'cn' :u'变压器与磁电工程师',
			'en' :'Transformer and Magnetoelectricity'
			},
		'110060' : {
			'cn' :u'家用电器/数码产品研发',
			'en' :'Household Electronics/Digital Products Development'
			},
		'110360' : {
			'cn' :u'电池/电源开发',
			'en' :'Battery/Power Engineer'
			},
		'110020' : {
			'cn' :u'电子/电器工程师',
			'en' :'Electronic/Electrical Equipment Engineer'
			},
		'110408' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'110090' : {
			'cn' :u'半导体技术',
			'en' :'Semiconductor Technology'
			},
		'110170' : {
			'cn' :u'电气工程师',
			'en' :'Electrical Engineer'
			},
		'110400' : {
			'cn' :u'电气线路设计',
			'en' :'Electrical Circuit Design'
			},
		'110401' : {
			'cn' :u'线路结构设计',
			'en' :'Route structure design'
			},
		'110402' : {
			'cn' :u'机电工程师',
			'en' :'Electrical & Mechanical Engineer'
			},
		'110010' : {
			'cn' :u'电路工程师/技术员',
			'en' :'Electronic Circuit Engineer'
			},
		'110404' : {
			'cn' :u'模拟电路设计/应用工程师',
			'en' :'Analogical Electronic Design / Application Engineer'
			},
		'110405' : {
			'cn' :u'空调工程/设计',
			'en' :'Air Conditioning Engineering/Design'
			},
		'110406' : {
			'cn' :u'仪器/仪表/计量',
			'en' :'Instrument/Measurement Analyst'
			},
		'110407' : {
			'cn' :u'安防系统工程师',
			'en' :'Security Systems Engineer'
			},
		'110130' : {
			'cn' :u'集成电路IC设计/应用工程师',
			'en' :'IC Design/Application Engineer'
			},
		'110120' : {
			'cn' :u'光源与照明工程师',
			'en' :'Light Source and Lighting Engineer'
			},
		'110110' : {
			'cn' :u'电子/电器维修',
			'en' :'Electronics/Electronics Repair'
			},
		'110310' : {
			'cn' :u'射频工程师',
			'en' :'RF Engineer'
			},
		'110350' : {
			'cn' :u'自动控制工程师/技术员',
			'en' :'Autocontrol Engineer/Technician'
			},
		'110330' : {
			'cn' :u'版图设计工程师',
			'en' :'Engineer Layout Design Engineer'
			},
		'110370' : {
			'cn' :u'FAE现场应用工程师',
			'en' :'Field Application Engineer(FAE)'
			},
		'110050' : {
			'cn' :u'电声/音响工程师/技术员',
			'en' :'Electroacoustics Engineer'
			},
		'110140' : {
			'cn' :u'技术文档工程师',
			'en' :'Technical Documentation Engineer'
			},
		'110380' : {
			'cn' :u'IC验证工程师',
			'en' :'IC Verification Engineer'
			},
		'110180' : {
			'cn' :u'电子技术研发工程师',
			'en' :'Electronics Development Engineer'
			},
	},
	'420' : {
		'420008' : {
			'cn' :u'汽车底盘/总装工程师',
			'en' :'Automobile Chassis/Assembly Engineer'
			},
		'420009' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'420001' : {
			'cn' :u'汽车项目管理',
			'en' :'Automotive Project Management'
			},
		'420002' : {
			'cn' :u'汽车机构工程师',
			'en' :'Automotive Structural Engineer'
			},
		'420003' : {
			'cn' :u'汽车设计工程师',
			'en' :'Automotive Design Engineer'
			},
		'420004' : {
			'cn' :u'汽车电子工程师',
			'en' :'Automotive Electronic Engineer'
			},
		'420005' : {
			'cn' :u'汽车质量工程师',
			'en' :'Automotive Quality Engineer'
			},
		'420006' : {
			'cn' :u'汽车安全性能工程师',
			'en' :'Safety Performance Engineer'
			},
		'420007' : {
			'cn' :u'汽车装配工艺工程师',
			'en' :'Assembly Engineer'
			},
		'420010' : {
			'cn' :u'汽车动力系统工程师',
			'en' :'Automobile Power System Engineers'
			},
	},
	'480' : {
		'480002' : {
			'cn' :u'放映管理',
			'en' :'Projection Management'
			},
		'250130' : {
			'cn' :u'录音/音效师',
			'en' :'Recording/Audio Engineer'
			},
		'250120' : {
			'cn' :u'摄影/摄像',
			'en' :'Photographer/Videographer'
			},
		'480001' : {
			'cn' :u'后期制作',
			'en' :'Postproduction'
			},
		'250150' : {
			'cn' :u'演员/配音/模特',
			'en' :'Actor/Voice Actor/Model'
			},
		'250110' : {
			'cn' :u'导演/编导',
			'en' :'Director/Choreographer'
			},
		'250100' : {
			'cn' :u'影视策划/制作/发行',
			'en' :'Film Planning/Production/Distribution'
			},
		'250090' : {
			'cn' :u'艺术/设计总监',
			'en' :'Artistic/Design Director'
			},
		'480003' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'250140' : {
			'cn' :u'化妆师/造型师/服装/道具',
			'en' :'Makeup Artist/Image Designer/Wardrobe/Prop'
			},
		'250170' : {
			'cn' :u'经纪人/星探',
			'en' :'Entertainment Agent'
			},
		'250160' : {
			'cn' :u'主持人/播音员/DJ',
			'en' :'Host/Broadcaster/DJ'
			},
	},
	'360' : {
		'360230' : {
			'cn' :u'音效设计师',
			'en' :'Sound Effects Designer'
			},
		'360020' : {
			'cn' :u'运营经理/主管',
			'en' :'Operations Manager/Supervisor'
			},
		'360180' : {
			'cn' :u'游戏策划师',
			'en' :'Game Planner'
			},
		'360210' : {
			'cn' :u'特效设计师',
			'en' :'Special Effects Designer'
			},
		'360100' : {
			'cn' :u'电子商务总监',
			'en' :'E-Commerce Director'
			},
		'360290' : {
			'cn' :u'视觉设计总监/经理',
			'en' :'Visual Design Director/Manager'
			},
		'360040' : {
			'cn' :u'产品总监',
			'en' :'Product Director'
			},
		'360120' : {
			'cn' :u'电子商务专员',
			'en' :'E-Commerce Specialist'
			},
		'360250' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'360270' : {
			'cn' :u'用户研究总监/经理',
			'en' :'User Research Director/Manager'
			},
		'360060' : {
			'cn' :u'SEO搜索引擎优化',
			'en' :'SEO'
			},
		'100340' : {
			'cn' :u'网页设计/制作/美工',
			'en' :'Web Designer/Production/Creative'
			},
		'100071' : {
			'cn' :u'产品经理/主管',
			'en' :'Product Manager/Supervisor'
			},
		'350010' : {
			'cn' :u'UI设计师',
			'en' :'UI Designer'
			},
		'060210' : {
			'cn' :u'SEM搜索引擎营销',
			'en' :'SEM'
			},
		'360090' : {
			'cn' :u'网络推广专员',
			'en' :'Online Marketing Specialist'
			},
		'360190' : {
			'cn' :u'游戏界面设计师',
			'en' :'Game UI Designer'
			},
		'100320' : {
			'cn' :u'网站策划',
			'en' :'Site Planning'
			},
		'100300' : {
			'cn' :u'网站营运管理',
			'en' :'Web Operations Management'
			},
		'360220' : {
			'cn' :u'视觉设计师',
			'en' :'Visual Effects Designer'
			},
		'360150' : {
			'cn' :u'UE交互设计师',
			'en' :'UE Interaction Designer'
			},
		'360030' : {
			'cn' :u'运营专员',
			'en' :'Operations Specialist'
			},
		'360240' : {
			'cn' :u'三维/3D设计/制作',
			'en' :'Three-dimensional/3D Design/Production'
			},
		'360200' : {
			'cn' :u'Flash设计/开发',
			'en' :'Flash Designer/Developer'
			},
		'360070' : {
			'cn' :u'网络推广总监',
			'en' :'Online Marketing Director'
			},
		'360280' : {
			'cn' :u'用户研究员',
			'en' :'User Researcher'
			},
		'360050' : {
			'cn' :u'产品专员/助理',
			'en' :'Product Specialist/Assistant'
			},
		'360010' : {
			'cn' :u'运营总监',
			'en' :'Operations Director'
			},
		'360260' : {
			'cn' :u'交互设计总监/经理',
			'en' :'Interaction Design Director/Manager'
			},
		'360110' : {
			'cn' :u'电子商务经理/主管',
			'en' :'E-Commerce Manager/Supervisor'
			},
		'360080' : {
			'cn' :u'网络推广经理/主管',
			'en' :'Online Marketing Manager/Supervisor'
			},
		'100310' : {
			'cn' :u'网站编辑',
			'en' :'Website Editor'
			},
	},
	'320' : {
		'320030' : {
			'cn' :u'动物营养/饲料研发',
			'en' :'Animal nutrition/Feed Development'
			},
		'320040' : {
			'cn' :u'农艺师',
			'en' :'Agronomist'
			},
		'320050' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'340070' : {
			'cn' :u'园艺师',
			'en' :'Gardener/Horticulturist'
			},
		'320020' : {
			'cn' :u'畜牧师',
			'en' :'Animal Husbandry Technician'
			},
	},
	'630' : {
		'100260' : {
			'cn' :u'文档工程师',
			'en' :'Documentation Engineer'
			},
		'360328' : {
			'cn' :u'IT支持',
			'en' :'IT Surpport'
			},
		'360329' : {
			'cn' :u'运维总监',
			'en' :'OPS Director'
			},
		'100330' : {
			'cn' :u'网络工程师',
			'en' :'Network Engineer'
			},
		'360331' : {
			'cn' :u'系统工程师',
			'en' :'System Engineer'
			},
		'360330' : {
			'cn' :u'运维开发',
			'en' :'OPS Developer'
			},
		'100030' : {
			'cn' :u'信息技术经理/主管',
			'en' :'IT Manager/Supervisor'
			},
		'100190' : {
			'cn' :u'数据库管理员(DBA)',
			'en' :'Database Administrator'
			},
		'100180' : {
			'cn' :u'ERP实施顾问',
			'en' :'ERP Implementation'
			},
		'630010' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'100040' : {
			'cn' :u'信息技术专员',
			'en' :'Information Technology Specialist'
			},
		'360160' : {
			'cn' :u'运维工程师',
			'en' :'Maintenance Engineer'
			},
		'390001' : {
			'cn' :u'硬件维护工程师',
			'en' :'Hardware maintenance engineer'
			},
		'630020' : {
			'cn' :u'运维经理/主管',
			'en' :'OPS Manager/Supervisor'
			},
		'100230' : {
			'cn' :u'网络信息安全工程师',
			'en' :'Network and Information Security Engineer'
			},
	},
	'060' : {
		'060190' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'060020' : {
			'cn' :u'市场经理/主管',
			'en' :'Marketing Manager/Supervisor'
			},
		'060090' : {
			'cn' :u'产品经理/主管',
			'en' :'Product Manager/Supervisor'
			},
		'460005' : {
			'cn' :u'活动策划',
			'en' :'Event Planner'
			},
		'060110' : {
			'cn' :u'促销经理/主管',
			'en' :'Promotion Manager/ Supervisor'
			},
		'060060' : {
			'cn' :u'市场调研与分析',
			'en' :'Market Research and Analysis'
			},
		'060010' : {
			'cn' :u'市场总监',
			'en' :'Marketing Director'
			},
		'060202' : {
			'cn' :u'市场拓展专员/助理',
			'en' :'BD Specialist/Assistant'
			},
		'060203' : {
			'cn' :u'品牌经理/主管',
			'en' :'Brand Manager/Supervisor'
			},
		'060200' : {
			'cn' :u'市场专员/助理',
			'en' :'Marketing Specialist/Assistant'
			},
		'060201' : {
			'cn' :u'市场拓展经理/主管',
			'en' :'BD manager/Supervisor'
			},
		'060130' : {
			'cn' :u'市场企划经理/主管',
			'en' :'Marketing Planning Manager/Supervisor'
			},
		'060207' : {
			'cn' :u'市场企划专员/助理',
			'en' :'Marketing Planning Specialist/Assistant'
			},
		'060204' : {
			'cn' :u'产品专员/助理',
			'en' :'Product Specialist/Assistant'
			},
		'060205' : {
			'cn' :u'市场通路经理/主管',
			'en' :'Trade Marketing Manager/Supervisor'
			},
		'060206' : {
			'cn' :u'市场通路专员/助理',
			'en' :'Trade Marketing Specialist/Assistant'
			},
		'060208' : {
			'cn' :u'选址拓展/新店开发',
			'en' :'Site Development'
			},
		'060209' : {
			'cn' :u'品牌专员/助理',
			'en' :'Brand Specialist/Assistant'
			},
		'460006' : {
			'cn' :u'活动执行',
			'en' :'Event Excution'
			},
	},
	'080' : {
		'080020' : {
			'cn' :u'行政经理/主管/办公室主任',
			'en' :'Administration Manager/Supervisor'
			},
		'080021' : {
			'cn' :u'行政专员/助理',
			'en' :'Administration Specialist/Assistant'
			},
		'080010' : {
			'cn' :u'行政总监',
			'en' :'Executive Director'
			},
		'080080' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'080065' : {
			'cn' :u'后勤/总务',
			'en' :'Logistics/General Affairs'
			},
		'080060' : {
			'cn' :u'图书/资料/档案管理',
			'en' :'Document Keeper'
			},
		'080061' : {
			'cn' :u'助理/秘书/文员',
			'en' :'Executive Assistant/Secretary'
			},
		'080062' : {
			'cn' :u'前台/总机/接待',
			'en' :'Receptionist'
			},
		'080063' : {
			'cn' :u'电脑操作/打字/录入员',
			'en' :'Computer Operator/Typist'
			},
	},
	'140' : {
		'140160' : {
			'cn' :u'PE/VC投资',
			'en' :'Private Equity/Venture Capital'
			},
		'140148' : {
			'cn' :u'固定收益业务',
			'en' :'Fixed Income'
			},
		'140149' : {
			'cn' :u'零售客户服务',
			'en' :'Retail Banking'
			},
		'140144' : {
			'cn' :u'投资/理财顾问',
			'en' :'Investment/Financial Management Advisor'
			},
		'140145' : {
			'cn' :u'金融产品经理',
			'en' :'Financial Product Manager'
			},
		'140146' : {
			'cn' :u'基金管理',
			'en' :'Fund Management'
			},
		'140147' : {
			'cn' :u'行业研究',
			'en' :'Industry Research'
			},
		'140140' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'140141' : {
			'cn' :u'融资总监',
			'en' :'Treasury Director'
			},
		'140142' : {
			'cn' :u'融资专员/助理',
			'en' :'Treasury Executive/Assistant'
			},
		'140143' : {
			'cn' :u'股票/期货操盘手',
			'en' :'Stocks/Futures Operator'
			},
		'140040' : {
			'cn' :u'投资银行业务',
			'en' :'Investment Banking'
			},
		'140080' : {
			'cn' :u'风险管理/控制',
			'en' :'Risk Management/Control'
			},
		'140010' : {
			'cn' :u'证券/外汇/期货经纪人',
			'en' :'Securities/Foreign Exchange/Futures/Brokerage'
			},
		'140153' : {
			'cn' :u'机构客户服务',
			'en' :'Institutional Investor Service'
			},
		'140152' : {
			'cn' :u'证券投资',
			'en' :'Securities Investment/Portfolio Investment'
			},
		'140151' : {
			'cn' :u'经纪业务',
			'en' :'Brokerage'
			},
		'140150' : {
			'cn' :u'合规稽查',
			'en' :'Compliance And Audit'
			},
		'140030' : {
			'cn' :u'证券分析/金融研究',
			'en' :'Security Analysis/Financial Research'
			},
		'140154' : {
			'cn' :u'资产管理',
			'en' :'Asset Management'
			},
		'140070' : {
			'cn' :u'资产评估',
			'en' :'Asset Evaluation'
			},
		'140050' : {
			'cn' :u'融资经理/主管',
			'en' :'Treasury Manager/Supervisor'
			},
	},
	'300' : {
		'300010' : {
			'cn' :u'科研管理人员',
			'en' :'Research Management'
			},
		'300021' : {
			'cn' :u'公务员/事业单位人员',
			'en' :'Civil Servant'
			},
		'300020' : {
			'cn' :u'科研人员',
			'en' :'Researchers'
			},
		'300030' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'310010' : {
			'cn' :u'志愿者',
			'en' :'Volunteer'
			},
	},
	'563' : {
		'640050' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'640040' : {
			'cn' :u'典当业务',
			'en' :'Pawn Business'
			},
		'640030' : {
			'cn' :u'拍卖师',
			'en' :'Auctioneer'
			},
		'640020' : {
			'cn' :u'担保业务',
			'en' :'Guarantee Business'
			},
		'140157' : {
			'cn' :u'信托业务',
			'en' :'Trust'
			},
		'140155' : {
			'cn' :u'房地产信托/物业投资',
			'en' :'Real Estate Investment Trust/REITS'
			},
		'640010' : {
			'cn' :u'珠宝/收藏品鉴定',
			'en' :'Jewellery /Collection Appraiser'
			},
	},
	'440' : {
		'440003' : {
			'cn' :u'面料辅料开发',
			'en' :'Fabric/Accessories Development'
			},
		'440009' : {
			'cn' :u'质量管理/验货员(QA/QC)',
			'en' :'Quality Management QA/QC'
			},
		'440006' : {
			'cn' :u'服装/纺织/皮革工艺师',
			'en' :'Apparels/Textiles/Leather Goods Technologist'
			},
		'440007' : {
			'cn' :u'板房/楦头/底格出格师',
			'en' :'Shoe Tree Design'
			},
		'440004' : {
			'cn' :u'面料辅料采购',
			'en' :'Fabric/Accessories Purchasing'
			},
		'440005' : {
			'cn' :u'服装/纺织/皮革跟单',
			'en' :'Apparels/Textiles/Leather Goods Merchandiser'
			},
		'440011' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'440010' : {
			'cn' :u'电脑放码员',
			'en' :'Grading'
			},
		'440001' : {
			'cn' :u'服装/纺织设计总监',
			'en' :'Fashion/Textiles Design Director'
			},
		'240040' : {
			'cn' :u'服装/纺织设计',
			'en' :'Fashion/Textiles Designer'
			},
		'240050' : {
			'cn' :u'服装打样/制版',
			'en' :'Sample Production'
			},
	},
	'460' : {
		'460008' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'460009' : {
			'cn' :u'媒介策划',
			'en' :'Media Planning'
			},
		'460004' : {
			'cn' :u'媒介专员/助理',
			'en' :'Media Specialist/Assistant'
			},
		'460007' : {
			'cn' :u'媒介销售',
			'en' :'Media Sales'
			},
		'460001' : {
			'cn' :u'公关总监',
			'en' :'Public Relations Director'
			},
		'460002' : {
			'cn' :u'公关专员/助理',
			'en' :'Public Relations Specialist/Assistant'
			},
		'460003' : {
			'cn' :u'媒介经理/主管',
			'en' :'Media Manager/Supervisor'
			},
		'290100' : {
			'cn' :u'政府事务管理',
			'en' :'Government Affairs'
			},
		'060040' : {
			'cn' :u'公关经理/主管',
			'en' :'Public Relations Manager/Supervisor'
			},
	},
	'120' : {
		'120170' : {
			'cn' :u'光伏技术工程师',
			'en' :'Photovoltaic Technology Engineer'
			},
		'120150' : {
			'cn' :u'能源/矿产项目管理',
			'en' :'Energy/Mining Project Management'
			},
		'340050' : {
			'cn' :u'地质勘查/选矿/采矿',
			'en' :'Geological Exploration'
			},
		'120140' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'120110' : {
			'cn' :u'石油/天然气技术人员',
			'en' :'Oil/Gas Technician'
			},
		'120100' : {
			'cn' :u'空调/热能工程师',
			'en' :'Air-Conditioning/Energy Engineers'
			},
		'120090' : {
			'cn' :u'核力/火力工程师',
			'en' :'Nuclear Power/Fire Engineer'
			},
		'120060' : {
			'cn' :u'电力工程师/技术员',
			'en' :'Electric Power Engineer'
			},
		'120070' : {
			'cn' :u'电力维修技术员',
			'en' :'Electricity Maintenance Technician'
			},
		'120040' : {
			'cn' :u'输电线路工程师',
			'en' :'Transmission Line Engineer'
			},
		'120160' : {
			'cn' :u'冶金工程师',
			'en' :'Metallurgical Engineer'
			},
		'120080' : {
			'cn' :u'水利/水电工程师',
			'en' :'Water Resources/Water and Electric Engineer'
			},
	},
	'260' : {
		'260020' : {
			'cn' :u'幼教',
			'en' :'Preschool Education'
			},
		'260058' : {
			'cn' :u'文科教师',
			'en' :'Liberal Arts Teacher'
			},
		'260071' : {
			'cn' :u'培训师/讲师',
			'en' :'Teacher/Trainer'
			},
		'260010' : {
			'cn' :u'教学/教务管理人员',
			'en' :'Teaching/Educational Administration'
			},
		'260059' : {
			'cn' :u'外语教师',
			'en' :'Foreign language teacher'
			},
		'260051' : {
			'cn' :u'高中教师',
			'en' :'High School Teacher'
			},
		'260053' : {
			'cn' :u'初中教师',
			'en' :'Junior high school teacher'
			},
		'260052' : {
			'cn' :u'职业中专/技校教师',
			'en' :'Vocational Technical Secondary School/Technical School Teacher'
			},
		'260055' : {
			'cn' :u'音乐教师',
			'en' :'Music Teacher'
			},
		'260054' : {
			'cn' :u'小学教师',
			'en' :'Grade School Teacher'
			},
		'260057' : {
			'cn' :u'理科教师',
			'en' :'Science teacher'
			},
		'260030' : {
			'cn' :u'大学教师/教授',
			'en' :'Professor'
			},
		'260073' : {
			'cn' :u'培训助理/助教',
			'en' :'Training Assistant'
			},
		'260056' : {
			'cn' :u'美术教师',
			'en' :'Art Teacher'
			},
		'260072' : {
			'cn' :u'培训督导',
			'en' :'Supervision Training'
			},
		'260070' : {
			'cn' :u'体育教师/教练',
			'en' :'Physical Teacher/Coach'
			},
		'260077' : {
			'cn' :u'教育产品开发',
			'en' :'Education Product Development'
			},
		'260075' : {
			'cn' :u'培训策划',
			'en' :'Training Planning'
			},
		'260074' : {
			'cn' :u'培训/招生/课程顾问',
			'en' :'Enrollment/Course Consultant'
			},
		'260009' : {
			'cn' :u'校长',
			'en' :'School Principal'
			},
		'260080' : {
			'cn' :u'其他',
			'en' :'Others'
			},
	},
	'240' : {
		'240010' : {
			'cn' :u'平面设计经理/主管',
			'en' :'Graphic Design Manager/Supervisor'
			},
		'240130' : {
			'cn' :u'展示/陈列设计',
			'en' :'Exhibition/Display Design'
			},
		'240155' : {
			'cn' :u'玩具设计',
			'en' :'Toy Design'
			},
		'240150' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'240110' : {
			'cn' :u'多媒体/动画设计',
			'en' :'Multimedia/Animation Design'
			},
		'240152' : {
			'cn' :u'绘画',
			'en' :'Graphic Illustrator'
			},
		'240153' : {
			'cn' :u'平面设计总监/经理',
			'en' :'Graphic Design Director/Manager'
			},
		'240125' : {
			'cn' :u'包装设计',
			'en' :'Packaging Design'
			},
		'240151' : {
			'cn' :u'创意指导/总监',
			'en' :'Creative Director/Director'
			},
		'240156' : {
			'cn' :u'CAD设计/制图',
			'en' :'CAD design/drafting'
			},
		'240157' : {
			'cn' :u'原画师',
			'en' :'Original Artist'
			},
		'240060' : {
			'cn' :u'工艺品/珠宝设计',
			'en' :'Crafts/Jewelry Design'
			},
		'240120' : {
			'cn' :u'3D设计/制作',
			'en' :'3D Design/Production'
			},
		'240030' : {
			'cn' :u'工业/产品设计',
			'en' :'Industrial/Product Design'
			},
		'240020' : {
			'cn' :u'美术/图形设计',
			'en' :'Art/Graphic Design'
			},
		'240090' : {
			'cn' :u'媒体广告设计',
			'en' :'Media Advertising'
			},
		'240080' : {
			'cn' :u'平面设计师',
			'en' :'Graphic Designer'
			},
		'240070' : {
			'cn' :u'家具/家居设计',
			'en' :'Furniture/Household Product Design'
			},
	},
	'280' : {
		'280020' : {
			'cn' :u'医疗技术人员',
			'en' :'Medical Technicians'
			},
		'280080' : {
			'cn' :u'疾病控制/公共卫生',
			'en' :'Disease Control/Public Health'
			},
		'280166' : {
			'cn' :u'外科医生',
			'en' :'Doctor Surgeial'
			},
		'280110' : {
			'cn' :u'药库主任/药剂师',
			'en' :'Drug Storehouse Director/Pharmacist'
			},
		'280010' : {
			'cn' :u'医院管理人员',
			'en' :'Hospital Management'
			},
		'280050' : {
			'cn' :u'医药学检验',
			'en' :'Clinical Laboratory'
			},
		'280171' : {
			'cn' :u'护理主任/护士长',
			'en' :'Nursing Officer'
			},
		'280172' : {
			'cn' :u'儿科医生',
			'en' :'Pediatrician'
			},
		'280173' : {
			'cn' :u'验光师',
			'en' :'Optometrist'
			},
		'280174' : {
			'cn' :u'放射科医师',
			'en' :'Radiologist'
			},
		'280175' : {
			'cn' :u'综合门诊/全科医生',
			'en' :'General Practitioner (GP)'
			},
		'280030' : {
			'cn' :u'理疗师',
			'en' :'Physical Therapist'
			},
		'280090' : {
			'cn' :u'美容/整形师',
			'en' :'Beautician/Plastic Surgeon'
			},
		'280167' : {
			'cn' :u'专科医生',
			'en' :'Doctor Specialist'
			},
		'280100' : {
			'cn' :u'兽医/宠物医生',
			'en' :'Veterinarian/Pet Doctor'
			},
		'280165' : {
			'cn' :u'营养师',
			'en' :'Dietitian'
			},
		'280164' : {
			'cn' :u'心理医生',
			'en' :'Psychologist/Psychiatrist'
			},
		'280163' : {
			'cn' :u'麻醉医生',
			'en' :'Anesthesiologist'
			},
		'280162' : {
			'cn' :u'护士/护理人员',
			'en' :'Nurse/Medical Assistant'
			},
		'280161' : {
			'cn' :u'内科医生',
			'en' :'Doctor Internal Medicine'
			},
		'280160' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'280120' : {
			'cn' :u'针灸推拿',
			'en' :'Acupuncture and Massage'
			},
		'280169' : {
			'cn' :u'中医科医生',
			'en' :'Chinese Medicine Practioners'
			},
		'280168' : {
			'cn' :u'牙科医生',
			'en' :'Dentist'
			},
	},
	'100' : {
		'360337' : {
			'cn' :u'配置管理工程师',
			'en' :'Configuration Management Engineer'
			},
		'360338' : {
			'cn' :u'配置管理经理/主管',
			'en' :'Configuration Management Manager/Supervisor'
			},
		'360324' : {
			'cn' :u'自动化测试',
			'en' :'Automation Testing Engineer'
			},
		'360325' : {
			'cn' :u'功能测试',
			'en' :'Functional Testing Engineer'
			},
		'360326' : {
			'cn' :u'性能测试',
			'en' :'Performance Testing Engineer'
			},
		'360327' : {
			'cn' :u'测试开发',
			'en' :'Test Development Engineer'
			},
		'100250' : {
			'cn' :u'硬件测试',
			'en' :'Hardware Testing'
			},
		'360322' : {
			'cn' :u'测试经理/主管',
			'en' :'Testing Manager/Supervisor'
			},
		'360323' : {
			'cn' :u'测试工程师',
			'en' :'Testing Engineer'
			},
		'100235' : {
			'cn' :u'计量/标准化工程师',
			'en' :'Measure/Standardization Engineer'
			},
		'100360' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'360340' : {
			'cn' :u'软件测试',
			'en' :'Software Testing'
			},
	},
	'160' : {
		'160050' : {
			'cn' :u'水运/空运/陆运操作',
			'en' :'Transport Operation'
			},
		'160190' : {
			'cn' :u'物流总监',
			'en' :'Logistics Director'
			},
		'160230' : {
			'cn' :u'物料专员/助理',
			'en' :'Materials Specialist/Assistant'
			},
		'160140' : {
			'cn' :u'货运代理',
			'en' :'Freight Forwarder'
			},
		'160200' : {
			'cn' :u'物流专员/助理',
			'en' :'Logistics Specialist/Assistant'
			},
		'160110' : {
			'cn' :u'物料经理/主管',
			'en' :'Materials Manager/Supervisor'
			},
		'160240' : {
			'cn' :u'集装箱业务',
			'en' :'Container Operator'
			},
		'160260' : {
			'cn' :u'单证员',
			'en' :'Documentation Specialist'
			},
		'160090' : {
			'cn' :u'物流经理/主管',
			'en' :'Logistics manager/Supervisor'
			},
		'160180' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'160040' : {
			'cn' :u'报关员',
			'en' :'Document Management/Customs Agent'
			},
		'160130' : {
			'cn' :u'运输经理/主管',
			'en' :'Transport Management/Executive'
			},
		'160120' : {
			'cn' :u'仓库经理/主管',
			'en' :'Warehouse Manager/Supervisor'
			},
		'160270' : {
			'cn' :u'物流/仓储项目管理',
			'en' :'Logistics/Warehousing Project Management'
			},
		'160160' : {
			'cn' :u'物流/仓储调度',
			'en' :'Logistics/Warehousing Dispatcher'
			},
		'160250' : {
			'cn' :u'海关事务管理',
			'en' :'Customs Affairs Management'
			},
	},
	'220' : {
		'220283' : {
			'cn' :u'船舶维修/保养',
			'en' :'Watercraft Repair/Maintenance'
			},
		'220090' : {
			'cn' :u'CNC工程师',
			'en' :'CNC Engineer'
			},
		'220005' : {
			'cn' :u'机械设备经理',
			'en' :'Mechanical Equipment Manager'
			},
		'220120' : {
			'cn' :u'锅炉工程师/技师',
			'en' :'Boiler Engineer'
			},
		'220250' : {
			'cn' :u'飞机维修/保养',
			'en' :'Aircraft Repair/Maintenance'
			},
		'220140' : {
			'cn' :u'列车设计与制造',
			'en' :'Train Design & Manufacture'
			},
		'220100' : {
			'cn' :u'冲压工程师/技师',
			'en' :'Punch Engineer'
			},
		'220020' : {
			'cn' :u'模具工程师',
			'en' :'Mold Engineer'
			},
		'220230' : {
			'cn' :u'工业工程师(IE)',
			'en' :'IE Engineer'
			},
		'220060' : {
			'cn' :u'精密机械',
			'en' :'Precision Machinery'
			},
		'220270' : {
			'cn' :u'轨道交通工程师/技师',
			'en' :'Railway Engineer/Technician'
			},
		'220160' : {
			'cn' :u'飞机设计与制造',
			'en' :'Aircraft Design & Manufacture'
			},
		'220040' : {
			'cn' :u'机械制图员',
			'en' :'Mechanical Draftsman'
			},
		'220210' : {
			'cn' :u'设备修理',
			'en' :'Equipment Repair'
			},
		'220080' : {
			'cn' :u'注塑工程师/技师',
			'en' :'Injection Engineer'
			},
		'220010' : {
			'cn' :u'机械工程师',
			'en' :'Mechanical Engineer'
			},
		'220130' : {
			'cn' :u'焊接工程师/技师',
			'en' :'Welding Engineer'
			},
		'220240' : {
			'cn' :u'机械结构工程师',
			'en' :'Mechanical Structural Engineer'
			},
		'220070' : {
			'cn' :u'铸造/锻造工程师/技师',
			'en' :'Casting/Forging Engineer'
			},
		'220110' : {
			'cn' :u'夹具工程师/技师',
			'en' :'Clamp Engineer'
			},
		'220281' : {
			'cn' :u'气动工程师',
			'en' :'Pneumatic Engineer'
			},
		'220282' : {
			'cn' :u'工艺/制程工程师(PE)',
			'en' :'PE Engineer'
			},
		'220030' : {
			'cn' :u'机械设计师',
			'en' :'Mechanical Designer'
			},
		'220284' : {
			'cn' :u'列车维修/保养',
			'en' :'Train Repair/Maintenance'
			},
		'220285' : {
			'cn' :u'机械设备工程师',
			'en' :'Mechanical Equipment Engineer'
			},
		'220200' : {
			'cn' :u'纺织机械',
			'en' :'Textile Machinery'
			},
		'220280' : {
			'cn' :u'材料工程师',
			'en' :'Material Engineer'
			},
		'220190' : {
			'cn' :u'食品机械',
			'en' :'Food Machinery'
			},
		'220220' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'120130' : {
			'cn' :u'制冷/暖通',
			'en' :'HVAC/Refrigeration'
			},
		'220150' : {
			'cn' :u'船舶设计与制造',
			'en' :'Watercraft Design & Manufacture'
			},
		'220260' : {
			'cn' :u'维修经理/主管',
			'en' :'Maintenance Manager/Supervisor'
			},
		'220050' : {
			'cn' :u'机电工程师',
			'en' :'Electrical and Mechanical Engineers'
			},
		'220170' : {
			'cn' :u'维修工程师',
			'en' :'Maintenance Engineer'
			},
	},
	'270' : {
		'270010' : {
			'cn' :u'律师',
			'en' :'Lawyer'
			},
		'270020' : {
			'cn' :u'法律顾问',
			'en' :'Legal Adviser'
			},
		'270060' : {
			'cn' :u'律师助理',
			'en' :'Paralegal'
			},
		'270043' : {
			'cn' :u'合规经理',
			'en' :'Compliance Manager'
			},
		'270042' : {
			'cn' :u'知识产权/专利/商标代理人',
			'en' :' Intellectual Property/Patent Advisor'
			},
		'270041' : {
			'cn' :u'法务专员/助理',
			'en' :'Lega Specialist/Assistant'
			},
		'270040' : {
			'cn' :u'法务经理/主管',
			'en' :'Legal manager/Supervisor'
			},
		'270050' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'270044' : {
			'cn' :u'合规主管/专员',
			'en' :'Compliance Supervisor/Specialist'
			},
	},
	'537' : {
		'380010' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'020100' : {
			'cn' :u'商务经理/主管',
			'en' :'Business Manager/Supervisor'
			},
		'380007' : {
			'cn' :u'销售培训讲师',
			'en' :'Sales trainer'
			},
		'380005' : {
			'cn' :u'销售运营专员/助理',
			'en' :'Sales Operations Executive/Assistant'
			},
		'380004' : {
			'cn' :u'销售运营经理/主管',
			'en' :'Sales Operations Manager/Supervisor'
			},
		'380003' : {
			'cn' :u'商务专员/助理',
			'en' :'Business Executive/Assistant'
			},
		'380002' : {
			'cn' :u'销售行政专员/助理',
			'en' :'Sales Admin. Executive/Assistant'
			},
		'380001' : {
			'cn' :u'销售行政经理/主管',
			'en' :'Sales Admin. Manager/Supervisor'
			},
		'380009' : {
			'cn' :u'业务分析专员/助理',
			'en' :'Business Analysis Specialist/Assistant'
			},
		'380008' : {
			'cn' :u'业务分析经理/主管',
			'en' :'Business Analysis Manager/Supervisor'
			},
	},
	'536' : {
		'370008' : {
			'cn' :u'医药销售代表',
			'en' :'Pharmaceutical Sales Representative'
			},
		'370009' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'370001' : {
			'cn' :u'销售代表',
			'en' :'Sales Representative'
			},
		'370002' : {
			'cn' :u'渠道/分销专员',
			'en' :'Channel/Distribution Representative'
			},
		'370003' : {
			'cn' :u'客户代表',
			'en' :'Sales Account Representative'
			},
		'370004' : {
			'cn' :u'销售工程师',
			'en' :'Sales Engineer'
			},
		'370005' : {
			'cn' :u'电话销售',
			'en' :'Telesales'
			},
		'370006' : {
			'cn' :u'经销商',
			'en' :'Distributor'
			},
		'370007' : {
			'cn' :u'大客户销售',
			'en' :'Key Account Sales'
			},
		'370013' : {
			'cn' :u'业务拓展专员/助理',
			'en' :'BD Specialist/Assistant'
			},
		'370012' : {
			'cn' :u'区域销售专员/助理',
			'en' :'Regional Sales Specialist/Assistant'
			},
		'370011' : {
			'cn' :u'网络/在线销售',
			'en' :'Online Sales'
			},
		'370010' : {
			'cn' :u'团购业务员',
			'en' :'Team Buying Sales'
			},
	},
	'535' : {
		'020005' : {
			'cn' :u'区域销售总监',
			'en' :'Regional Sales Director'
			},
		'020010' : {
			'cn' :u'销售总监',
			'en' :'Sales Director'
			},
		'020040' : {
			'cn' :u'渠道/分销总监',
			'en' :'Channel/Distribution Director'
			},
		'020126' : {
			'cn' :u'团购经理/主管',
			'en' :'Team Buying Manager/Supervisor'
			},
		'020125' : {
			'cn' :u'销售总经理/销售副总裁',
			'en' :'Sales General Manager/Vice President'
			},
		'020122' : {
			'cn' :u'客户经理/主管',
			'en' :'Sales Account Manager/Supervisor'
			},
		'020121' : {
			'cn' :u'大客户销售管理',
			'en' :'Key Account Sales Management'
			},
		'020120' : {
			'cn' :u'业务拓展经理/主管',
			'en' :'Business Development Supervisor/Manager'
			},
		'020020' : {
			'cn' :u'销售经理/主管',
			'en' :'Sales Manager/Supervisor'
			},
		'020050' : {
			'cn' :u'渠道/分销经理/主管',
			'en' :'Channel/Distribution Manager/Supervisor'
			},
		'020160' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'020127' : {
			'cn' :u'客户总监',
			'en' :'Account Director'
			},
		'020025' : {
			'cn' :u'区域销售经理/主管',
			'en' :'Regional Sales Manager/Supervisor'
			},
	},
	'130' : {
		'130020' : {
			'cn' :u'咨询总监',
			'en' :'Advisory Director'
			},
		'130010' : {
			'cn' :u'企管顾问/专业顾问/策划师',
			'en' :'Business Management/Consultant/Adviser/Professional Planner'
			},
		'130050' : {
			'cn' :u'调研员',
			'en' :'Researcher'
			},
		'130040' : {
			'cn' :u'咨询顾问/咨询员',
			'en' :'Consultant'
			},
		'130030' : {
			'cn' :u'咨询经理/主管',
			'en' :'Consulting Manager/Supervisor'
			},
		'130073' : {
			'cn' :u'咨询项目管理',
			'en' :'Consulting Project Management'
			},
		'130071' : {
			'cn' :u'情报信息分析师',
			'en' :'Intelligence Analyst'
			},
		'130070' : {
			'cn' :u'涉外咨询师',
			'en' :'Foreign Consultants'
			},
		'130060' : {
			'cn' :u'培训师',
			'en' :'Trainers'
			},
		'130080' : {
			'cn' :u'其他',
			'en' :'Others'
			},
	},
	'410' : {
		'410020' : {
			'cn' :u'信用卡中心',
			'en' :'Credit Card Center'
			},
		'410009' : {
			'cn' :u'大堂经理',
			'en' :'Hall Manager'
			},
		'410008' : {
			'cn' :u'综合业务专员/助理',
			'en' :'Integrated Service Executive/Assistant'
			},
		'140060' : {
			'cn' :u'客户经理/主管',
			'en' :'Account Manager/Supervisor'
			},
		'410003' : {
			'cn' :u'公司业务部门经理/主管',
			'en' :'Corporate Banking Manager'
			},
		'410002' : {
			'cn' :u'客户代表',
			'en' :'Account Representative'
			},
		'410001' : {
			'cn' :u'银行经理/主任',
			'en' :'Bank Manager/Supervisor'
			},
		'140020' : {
			'cn' :u'行长/副行长',
			'en' :'President/Vice-President/Branch Manager'
			},
		'410007' : {
			'cn' :u'综合业务经理/主管',
			'en' :'Integrated Service Manager/Supervisor'
			},
		'410006' : {
			'cn' :u'个人业务客户经理',
			'en' :'Personal Banking Account Manager'
			},
		'410005' : {
			'cn' :u'个人业务部门经理/主管',
			'en' :'Personal Banking Manager/Supervisor'
			},
		'410004' : {
			'cn' :u'公司业务客户经理',
			'en' :'Corporate Banking Account Manager'
			},
		'140100' : {
			'cn' :u'清算人员',
			'en' :'Settlement Officer'
			},
		'140120' : {
			'cn' :u'银行卡/电子银行/新业务开拓',
			'en' :'Bank card/Electronic Banking/New Business'
			},
		'410019' : {
			'cn' :u'基金托管',
			'en' :'Trust Fund'
			},
		'140110' : {
			'cn' :u'柜员/银行会计',
			'en' :'Bank Teller/Bank Accountan'
			},
		'410014' : {
			'cn' :u'资金管理',
			'en' :'Fund Management'
			},
		'410015' : {
			'cn' :u'行业研究',
			'en' :'Industry Research'
			},
		'410016' : {
			'cn' :u'资产管理',
			'en' :'Asset Management'
			},
		'410017' : {
			'cn' :u'金融同业',
			'en' :'Interbank'
			},
		'410010' : {
			'cn' :u'进出口/信用证结算',
			'en' :'Trading / LC Officer'
			},
		'410011' : {
			'cn' :u'风险控制',
			'en' :'Risk Management'
			},
		'410012' : {
			'cn' :u'信审核查',
			'en' :'Credit Review'
			},
		'410013' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'140130' : {
			'cn' :u'国际结算/外汇交易',
			'en' :'International Account Settlement/Foreign Exchange'
			},
		'410022' : {
			'cn' :u'客户总监',
			'en' :'Account Director'
			},
		'140090' : {
			'cn' :u'信贷管理/资信评估/分析',
			'en' :'Loan/Credit Officer、Assets/Credit Valuation/Analyst'
			},
	},
	'290' : {
		'290080' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'290101' : {
			'cn' :u'招投标管理',
			'en' :'Tendering Coordinator'
			},
		'290020' : {
			'cn' :u'临床研究员',
			'en' :'Clinical Researcher'
			},
		'290030' : {
			'cn' :u'药品研发',
			'en' :'Medicine R&D'
			},
		'290055' : {
			'cn' :u'医疗器械市场推广',
			'en' :'Medical Equipment Marketing'
			},
		'290093' : {
			'cn' :u'医药销售经理/主管',
			'en' :'Pharmaceutical Sales Manager'
			},
		'290102' : {
			'cn' :u'医药招商经理/主管',
			'en' :'Pharmaceutical Business Development Manager/Supervisor'
			},
		'280150' : {
			'cn' :u'医药代表',
			'en' :'Medical Representative'
			},
		'290092' : {
			'cn' :u'药品市场推广专员/助理',
			'en' :'Pharmaceutical Promotion Specialist/Assistant'
			},
		'280070' : {
			'cn' :u'医药技术研发管理人员',
			'en' :'Pharmaceutical Technology R&D Management'
			},
		'290090' : {
			'cn' :u'临床数据分析员',
			'en' :'Clinical Data Analyst'
			},
		'290091' : {
			'cn' :u'药品市场推广经理/主管',
			'en' :'Pharmaceutical Promotion Manager/Supervisor'
			},
		'290096' : {
			'cn' :u'化学分析测试员',
			'en' :'Chemical Analyst'
			},
		'290040' : {
			'cn' :u'药品生产/质量管理',
			'en' :'Drug Manufacturing/Quality Management'
			},
		'290094' : {
			'cn' :u'医疗器械研发',
			'en' :'Medical Equipment R&D'
			},
		'290095' : {
			'cn' :u'医疗器械注册',
			'en' :'Medical Equipment Registration'
			},
		'290010' : {
			'cn' :u'生物工程/生物制药',
			'en' :'Biopharmaceutical/Biotechnology'
			},
		'290099' : {
			'cn' :u'医药招商专员/助理',
			'en' :'Pharmaceutical Business Development Specialist/Assistant'
			},
		'280130' : {
			'cn' :u'药品注册',
			'en' :'Drug Registration'
			},
		'290098' : {
			'cn' :u'医疗器械销售代表',
			'en' :'Medical Equipment Sales'
			},
		'290097' : {
			'cn' :u'医疗器械生产/质量管理',
			'en' :'Medical Equipment Manufacturing/Quality Control'
			},
	},
	'350' : {
		'100290' : {
			'cn' :u'多媒体/游戏开发工程师',
			'en' :'Multimedia/Game Development Engineer'
			},
		'360310' : {
			'cn' :u'移动开发工程师',
			'en' :'Mobile Development Engineer'
			},
		'360300' : {
			'cn' :u'WEB前端开发工程师',
			'en' :'WEB Front-end Developer'
			},
		'350040' : {
			'cn' :u'需求分析师',
			'en' :'Demand Analyst'
			},
		'100350' : {
			'cn' :u'计算机辅助设计工程师',
			'en' :'Computer Aided Design Engineer'
			},
		'360333' : {
			'cn' :u'数据库开发工程师',
			'en' :'Database Developer'
			},
		'360320' : {
			'cn' :u'BI工程师',
			'en' :'Business Intelligence Engineer'
			},
		'100100' : {
			'cn' :u'高级软件工程师',
			'en' :'Senior Software Engineer'
			},
		'360321' : {
			'cn' :u'架构师',
			'en' :'Architect'
			},
		'100090' : {
			'cn' :u'软件工程师',
			'en' :'Software Engineer'
			},
		'100080' : {
			'cn' :u'系统分析师',
			'en' :'System Analyst'
			},
		'360336' : {
			'cn' :u'数据挖掘工程师',
			'en' :'Data Mining Engineer'
			},
		'350030' : {
			'cn' :u'ERP技术开发',
			'en' :'ERP R&D'
			},
		'350020' : {
			'cn' :u'仿真应用工程师',
			'en' :'Simulation Application Engineer'
			},
		'110070' : {
			'cn' :u'嵌入式软件开发',
			'en' :'Embedded Software Engineer'
			},
		'360332' : {
			'cn' :u'数据分析师',
			'en' :'Data Analyst'
			},
		'100140' : {
			'cn' :u'系统集成工程师',
			'en' :'Systems Integration Engineer'
			},
		'100280' : {
			'cn' :u'语音/视频/图形开发工程师',
			'en' :'Audio/Video/Graphics Development Engineer'
			},
		'360334' : {
			'cn' :u'算法工程师',
			'en' :'Algorithm Engineer'
			},
		'350070' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'360335' : {
			'cn' :u'移动前端开发工程师',
			'en' :'Mobile Front-end Developer'
			},
	},
	'510' : {
		'510009' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'170070' : {
			'cn' :u'房地产项目策划经理/主管',
			'en' :'Real Estate Planning Manager/Supervisor'
			},
		'510001' : {
			'cn' :u'房地产项目策划专员/助理',
			'en' :'Real Estate Planning Specialist/Assistant'
			},
		'510002' : {
			'cn' :u'配套经理/主管',
			'en' :'Real Estate Supporting Manager/Supervisor'
			},
		'510003' : {
			'cn' :u'房地产项目招投标',
			'en' :'Real Estate Tender /Bidding'
			},
		'510004' : {
			'cn' :u'房地产投资分析',
			'en' :'Real Estate Investment Analysis'
			},
		'510005' : {
			'cn' :u'房地产资产管理',
			'en' :'Real Estate Asset Management'
			},
		'510017' : {
			'cn' :u'房地产项目运营',
			'en' :'Real Estate Project Operation'
			},
		'510016' : {
			'cn' :u'房地产项目管理',
			'en' :'Real Estate Project Management'
			},
		'510015' : {
			'cn' :u'成本经理/主管',
			'en' :'Cost Accounting Manager/Supervisor'
			},
		'510014' : {
			'cn' :u'成本总监',
			'en' :'Cost Accounting Director'
			},
		'170204' : {
			'cn' :u'开发报建专员/助理',
			'en' :'Applying for Construction Specialist/Assistant'
			},
		'510012' : {
			'cn' :u'规划设计师',
			'en' :'Planning Designer'
			},
		'510011' : {
			'cn' :u'规划设计总监',
			'en' :'Planning Director'
			},
		'510010' : {
			'cn' :u'配套工程师',
			'en' :'Real Estate Supporting Engineer'
			},
		'170198' : {
			'cn' :u'开发报建经理/主管',
			'en' :'Applying for Construction Manager/Supervisor'
			},
		'510019' : {
			'cn' :u'规划设计经理/主管',
			'en' :'Planning Manager/Supervisor'
			},
	},
	'291' : {
		'291010' : {
			'cn' :u'店长/卖场管理',
			'en' :'Store Manager/Floor Manager'
			},
		'291031' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'291030' : {
			'cn' :u'生鲜食品加工/处理',
			'en' :'Raw Food Assistant'
			},
		'291020' : {
			'cn' :u'店员/营业员',
			'en' :'Store Manager Trainee/Salesperson'
			},
		'291050' : {
			'cn' :u'安防主管',
			'en' :'Security Technical Service Executive'
			},
		'291040' : {
			'cn' :u'品类管理',
			'en' :'Category Management'
			},
	},
	'292' : {
		'292050' : {
			'cn' :u'列车乘务',
			'en' :'Train Crew'
			},
		'292010' : {
			'cn' :u'航空乘务',
			'en' :'Airline Crew'
			},
		'292060' : {
			'cn' :u'船员/水手',
			'en' :'Sailor/Shipmate'
			},
		'292070' : {
			'cn' :u'船舶乘务',
			'en' :'Shipping Service'
			},
		'292020' : {
			'cn' :u'地勤人员',
			'en' :'Ground Attendant'
			},
		'292030' : {
			'cn' :u'船长/副船长',
			'en' :'Fleet Captain'
			},
		'292031' : {
			'cn' :u'汽车司机',
			'en' :'Car Driver'
			},
		'292040' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'340018' : {
			'cn' :u'列车车长/司机',
			'en' :'Train Driver'
			},
		'340015' : {
			'cn' :u'飞机机长/副机长',
			'en' :'Flight Captain'
			},
	},
	'430' : {
		'430011' : {
			'cn' :u'汽车定损/车险理赔',
			'en' :'Automobile Insurance'
			},
		'430009' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'430008' : {
			'cn' :u'二手车评估师',
			'en' :'Second-Hand Car Appraisers'
			},
		'430010' : {
			'cn' :u' 汽车维修/保养',
			'en' :'Automobile Repair/Maintenance'
			},
		'430001' : {
			'cn' :u'汽车销售',
			'en' :'Automobile Sales'
			},
		'430003' : {
			'cn' :u'4S店管理',
			'en' :'4S Shop Management'
			},
		'430002' : {
			'cn' :u'售后服务客户服务',
			'en' :'After-Sales Service/Customer Service'
			},
		'430005' : {
			'cn' :u'装饰美容',
			'en' :'Decoration'
			},
		'430004' : {
			'cn' :u'零配件销售',
			'en' :'Parts Sales'
			},
		'430007' : {
			'cn' :u'检验检测',
			'en' :'Check/Test'
			},
		'430006' : {
			'cn' :u'汽车质量管理',
			'en' :'Automotive Quality Management'
			},
	},
	'538' : {
		'030060' : {
			'cn' :u'售后支持经理/主管',
			'en' :'After-Sales Support Manager/Supervisor'
			},
		'030070' : {
			'cn' :u'售后支持工程师',
			'en' :'Sales Support Engineer'
			},
		'030085' : {
			'cn' :u'客户服务经理/主管',
			'en' :'Customer Service Manager/Specialist'
			},
		'030084' : {
			'cn' :u'会员/VIP管理',
			'en' :'VIP Member Management'
			},
		'030086' : {
			'cn' :u'网络/在线客服',
			'en' :'Online Customer Service'
			},
		'030081' : {
			'cn' :u'客户服务专员/助理',
			'en' :'Customer Service Specialist/Assistant'
			},
		'030080' : {
			'cn' :u'其他',
			'en' :'Others'
			},
		'030083' : {
			'cn' :u'投诉处理专员',
			'en' :'Complaint Coordinator'
			},
		'030082' : {
			'cn' :u'咨询热线/呼叫中心人员',
			'en' :'Hotline/Call Center Staff'
			},
		'360130' : {
			'cn' :u'网店店长/客服管理',
			'en' :'Online Shop Manager/Customer Service Management'
			},
		'030010' : {
			'cn' :u'客户服务总监',
			'en' :'Director of Customer Service'
			},
		'020080' : {
			'cn' :u'售前支持工程师',
			'en' :'Pre-Sales Support Engineer'
			},
		'020070' : {
			'cn' :u'售前支持经理/主管',
			'en' :'Pre-Sales Support Manager/Supervisor'
			}
	}
}
