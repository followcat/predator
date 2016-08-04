# -*- coding: utf-8 -*-
import jieba


tags = {
    u'美术': 'Art',
    u'包装': 'Packaging',
    u'工艺': 'Process',
    u'咨询': 'Consultant',
    u'图形': 'Graphic',
    u'仿真': 'Simulation',
    u'总监': 'Director',
    u'通信': 'Communication',
    u'维修': 'Maintenance',
    u'科研人员': 'Researchers',
    u'监理': 'Management',
    u'保险': 'Insurance',
    u'珠宝': 'Jewelry',
    u'服务': 'Service',
    u'EHS': 'EHS',
    u'品牌': 'Brand',
    u'音效': 'Audio',
    u'员': 'Inspector',
    u'暖通': 'Refrigeration',
    u'调研': 'Research',
    u'关系': 'Relations',
    u'事务管理': 'Affairs',
    u'电子商务': 'E-Commerce',
    u'工程': 'Engineering',
    u'网站': 'Site',
    u'安防': 'Security',
    u'会务': 'Exhibition',
    u'技术': 'Techonlogy',
    u'客服': 'Service',
    u'技术人员': 'Technician',
    u'排版': 'Layout',
    u'标准化': 'Standardization',
    u'德语': 'German',
    u'宠物': 'Pet',
    u'文员': 'Clerk',
    u'票务': 'Ticket',
    u'摄像': 'Videographer',
    u'3D': '3D',
    u'岩土': 'Geotechnical',
    u'公路': 'Road',
    u'技术': 'Technical',
    u'中国': 'Chinese',
    u'金融': 'Finance',
    u'摄影': 'Photographer',
    u'播音员': 'Broadcaster',
    u'检验': 'Laboratory',
    u'美工': 'Creative',
    u'法语': 'French',
    u'翻译': 'Translator',
    u'调墨': 'Ink',
    u'商务': 'Business',
    u'区域': 'Regional',
    u'产品': 'Product',
    u'分析': 'Analysis',
    u'控制': 'Management',
    u'经销商': 'Distributor',
    u'宴会': 'Banquet',
    u'人力资源': 'HR',
    u'理疗': 'Physical',
    u'验光师': 'Optometrist',
    u'兽医': 'Veterinarian',
    u'三维': 'Three-dimensional',
    u'仓储': 'Warehouse',
    u'电器': 'Wiring',
    u'半导体': 'Semiconductor',
    u'典当': 'Pawn',
    u'泰语': 'Thai',
    u'需求': 'Demand',
    u'录入员': 'Typist',
    u'货运': 'Freight',
    u'主持人': 'Host',
    u'纺织': 'Textiles',
    u'葡萄牙语': 'Portuguese',
    u'计量': 'Analyst',
    u'面料': 'Fabric',
    u'组稿': 'Editor',
    u'语音': 'Audio',
    u'方言': 'Dialect',
    u'软件': 'Software',
    u'部门经理': 'Manager',
    u'ERP': 'ERP',
    u'技师': 'Technician',
    u'交换': 'Exchange',
    u'分析师': 'Analyst',
    u'医院': 'Hospital',
    u'气动': 'Pneumatic',
    u'督导': 'Training',
    u'CAD': 'CAD',
    u'石油': 'Oil',
    u'管理人员': 'Management',
    u'楼宇': 'Building',
    u'教学': 'Teaching',
    u'环境': 'Environmental',
    u'电源': 'Power',
    u'西班牙语': 'Spanish',
    u'水手': 'Shipmate',
    u'CFO': 'CFO',
    u'酒店': 'Hospitality',
    u'秘书': 'Assistant',
    u'代理': 'Forwarder',
    u'拓展': 'Development',
    u'工厂': 'Plant',
    u'情报信息': 'Intelligence',
    u'地质': 'Geological',
    u'领班': 'Supervisor',
    u'综合': 'Integrated',
    u'审计': 'Audit',
    u'牙科医生': 'Dentist',
    u'设施': 'Establishment',
    u'加工': 'Food',
    u'处理': 'Treatment',
    u'师': 'Surgeon',
    u'放映': 'Projection',
    u'清算': 'Settlement',
    u'服装': 'Fashion',
    u'飞机': 'Aircraft',
    u'通路': 'Marketing',
    u'化工': 'Chemical',
    u'销售': 'Sales',
    u'渠道': 'Channel',
    u'水': 'Water',
    u'执行': 'Excution',
    u'医药学': 'Clinical',
    u'产品': 'Product',
    u'售前': 'Pre-Sales',
    u'饲料': 'Feed',
    u'仪器': 'Instrument',
    u'茶艺': 'Tea',
    u'规划': 'Estate',
    u'印刷': 'Printing',
    u'医疗': 'Medicine',
    u'银行卡': 'Bank',
    u'桥梁': 'and',
    u'天然气': 'Gas',
    u'教务': 'Educational',
    u'VIP': 'Member',
    u'教育': 'Education',
    u'出纳员': 'Cashier',
    u'干部': 'Trainee',
    u'策划': 'Planner',
    u'制冷': 'HVAC',
    u'客户服务': 'Banking',
    u'托管': 'Fund',
    u'防护': 'Protection',
    u'电路': 'Electronic',
    u'计划': 'Planning',
    u'大堂': 'Lobby',
    u'体系': 'Systems',
    u'网页': 'Web',
    u'审核员': 'Auditor',
    u'陈列': 'Display',
    u'整形': 'Plastic',
    u'司机': 'Driver',
    u'影视': 'Film',
    u'列车': 'Train',
    u'生物工程': 'Biopharmaceutical',
    u'实施': 'Implementation',
    u'护理': 'Nursing',
    u'交互': 'Interaction',
    u'医生': 'Doctor',
    u'员工': 'Employee',
    u'传输': 'Transmission',
    u'交通': 'Transportation',
    u'制造': 'Manufacturing',
    u'临床': 'Clinical',
    u'资金': 'Fund',
    u'银行': 'Electronic',
    u'统计员': 'Statistician',
    u'船员': 'Sailor',
    u'实习生': 'Intern',
    u'证券': 'Security',
    u'建筑': 'Building',
    u'电气': 'Electrical',
    u'音乐': 'Music',
    u'投资': 'Investments',
    u'志愿者': 'Volunteer',
    u'电池': 'Battery',
    u'厂长': 'Manager',
    u'DJ': 'DJ',
    u'展示': 'Exhibition',
    u'招聘': 'Recruiting',
    u'线路': 'Circuit',
    u'银行业务': 'Banking',
    u'应用': 'Application',
    u'拍卖师': 'Auctioneer',
    u'移动': 'Mobile',
    u'法务': 'Legal',
    u'大': 'Key',
    u'讲师': 'Trainer',
    u'机械设备': 'Mechanical',
    u'婚礼': 'Wedding',
    u'集装箱': 'Container',
    u'医疗器械': 'Medical',
    u'工艺品': 'Crafts',
    u'测试': 'Testing',
    u'算法': 'Algorithm',
    u'写作': 'Writing',
    u'企业': 'Corporate',
    u'室内装潢': 'Interior',
    u'分析员': 'Analyst',
    u'合规': 'Compliance',
    u'导演': 'Director',
    u'律师': 'Lawyer',
    u'测量': 'Surveyor',
    u'营运': 'Operation',
    u'人员': 'Sales',
    u'画师': 'Artist',
    u'媒介': 'Media',
    u'培训': 'Training',
    u'售后': 'After-Sales',
    u'教练': 'Coach',
    u'Flash': 'Flash',
    u'电子': 'card',
    u'设计': 'Design',
    u'宾客': 'Guest',
    u'研究员': 'Researcher',
    u'融资': 'Treasury',
    u'后期制作': 'Postproduction',
    u'工程师': 'Engineer',
    u'配置管理': 'Management',
    u'高级': 'Senior',
    u'其他': 'Others',
    u'星探': 'Agent',
    u'WEB': 'WEB',
    u'财务': 'Financial',
    u'健身': 'Fitness',
    u'零售': 'Retail',
    u'编辑': 'Editor',
    u'客户': 'Account',
    u'仪表': 'Measurement',
    u'模具': 'Mold',
    u'科学': 'Science',
    u'健康': 'Health',
    u'前端': 'Front-end',
    u'通讯': 'Communications',
    u'隧道': 'Tunnel',
    u'土建': 'Planning',
    u'资产': 'Asset',
    u'材料': 'Material',
    u'打字': 'Operator',
    u'网络': 'Online',
    u'律师助理': 'Paralegal',
    u'制作': 'Production',
    u'媒体广告': 'Media',
    u'电话': 'Telephone',
    u'农艺师': 'Agronomist',
    u'顾问': 'Advisor',
    u'美容': 'Beautician',
    u'视觉': 'Visual',
    u'矿产': 'Mining',
    u'医药': 'Medical',
    u'文案': 'Copywriter',
    u'管理': 'Management',
    u'机构': 'Structural',
    u'硬件': 'Hardware',
    u'广告创意': 'Advertising',
    u'文档': 'Documentation',
    u'质量': 'Quality',
    u'零配件': 'Parts',
    u'评价': 'Assessment',
    u'采购': 'Purchasing',
    u'基金': 'Trust',
    u'市场': 'Trade',
    u'教师': 'Teacher',
    u'咨询师': 'Consultants',
    u'项目': 'Project',
    u'招投标': 'Tendering',
    u'股票': 'Stocks',
    u'及': 'and',
    u'担保': 'Guarantee',
    u'道路': 'Road',
    u'行政': 'Admin.',
    u'运输': 'Transport',
    u'系统': 'Systems',
    u'电脑操作': 'Computer',
    u'广告': 'Advertising',
    u'营养师': 'Dietitian',
    u'外贸': 'Trading',
    u'平面': 'Graphic',
    u'测绘': 'Mapping',
    u'房地产': 'Real',
    u'结算': 'Cost',
    u'故障': 'Failure',
    u'认证': 'Certification',
    u'原': 'Original',
    u'出版': 'Publishing',
    u'能源': 'Energy',
    u'轨道交通': 'Railway',
    u'注册': 'Registration',
    u'签证': 'Visa',
    u'理科': 'Science',
    u'多媒体': 'Multimedia',
    u'研究': 'Research',
    u'涉外': 'Foreign',
    u'电信': 'Telecommunication',
    u'自动化': 'Automation',
    u'农业': 'Agriculture',
    u'农林牧渔': 'Agriculture',
    u'电分': 'Operator-Colour',
    u'船舶': 'Watercraft',
    u'分销': 'Distribution',
    u'有线': 'Wired',
    u'经纪人': 'Entertainment',
    u'首席': 'Chief',
    u'勘查': 'Survey',
    u'管理员': 'Manager',
    u'工会': 'Unions',
    u'维护': 'maintenance',
    u'发行': 'Distribution',
    u'评估': 'Evaluation',
    u'代表': 'Sales',
    u'元器件': 'Component',
    u'供应商': 'Supplier',
    u'编导': 'Choreographer',
    u'光伏': 'Photovoltaic',
    u'官': 'Officer',
    u'创意': 'Creative',
    u'涂料': 'R&D',
    u'俄语': 'Russian',
    u'生活': 'Life',
    u'机械': 'Machine',
    u'新': 'Banking',
    u'土木': 'Civil',
    u'策划师': 'Planner',
    u'助理': 'Assistant',
    u'艺术': 'Art',
    u'在线': 'Customer',
    u'电力': 'Electric',
    u'信息技术': 'IT',
    u'光电子': 'Optoelectronics',
    u'IC': 'IC',
    u'制图': 'drafting',
    u'物业': 'Property',
    u'机长': 'Operator',
    u'操盘手': 'Operator',
    u'架构师': 'Architect',
    u'交通运输': 'Traffic',
    u'乘务': 'Crew',
    u'主任': 'Supervisor',
    u'税务': 'Taxation',
    u'激光': 'Laser',
    u'调研员': 'Researcher',
    u'BI': 'BI',
    u'生鲜食品': 'Raw',
    u'楼面': 'Floor',
    u'合同': 'Contract',
    u'契约': 'Policy',
    u'机电': 'Electrical',
    u'调酒师': 'Bartender',
    u'专员': 'Specialist',
    u'塑料': 'Plastics',
    u'阿拉伯语': 'Arabic',
    u'组长': 'Group',
    u'生产': 'Production',
    u'结构': 'Structural',
    u'录音': 'Recording',
    u'汽车': 'Automotive',
    u'餐饮': 'Restaurant',
    u'物料': 'Material',
    u'政府': 'Government',
    u'操作员': 'Distinguishing',
    u'装潢': 'Decoration',
    u'投资者': 'Investor',
    u'品类': 'Category',
    u'采编': 'Newspaper',
    u'市场': 'Marketing',
    u'修理': 'Repair',
    u'环保': 'Environmental',
    u'会员': 'VIP',
    u'造价': 'Cost',
    u'会展': 'Exhibition',
    u'安装': 'Installation',
    u'爆破': 'Blast',
    u'游戏': 'Game',
    u'冶金': 'Metallurgical',
    u'系统集成': 'Integration',
    u'公务员': 'Official',
    u'成本': 'Capital',
    u'水质': 'Water',
    u'物流': 'Logistics',
    u'机械制图': 'Mechanical',
    u'设备': 'Equipment',
    u'再保险': 'Reinsurance',
    u'意大利语': 'Italian',
    u'输电': 'Transmission',
    u'辅料': 'Accessories',
    u'玩具': 'Toy',
    u'自动控制': 'Autocontrol',
    u'调度': 'Dispatcher',
    u'空调': 'Air-Conditioning',
    u'厨师': 'Chef',
    u'UI': 'UI',
    u'UE': 'UE',
    u'储备': 'Associate',
    u'娱乐': 'Entertainmen',
    u'风险': 'Risk',
    u'检测': 'Quality',
    u'化妆品': 'Cosmetics',
    u'预定': 'Reservation',
    u'预算': 'Bridge',
    u'设计师': 'Designer',
    u'无线': 'RF',
    u'预': 'Budget',
    u'数据分析': 'Data',
    u'科研': 'Research',
    u'仓库': 'Warehouse',
    u'协调': 'Coordination',
    u'保养': 'Maintenance',
    u'安全': 'Safety',
    u'数据': 'Data',
    u'视频': 'Video',
    u'会计': 'Accounting',
    u'个人': 'Personal',
    u'用户': 'User',
    u'药品': 'Drug',
    u'营养': 'nutrition',
    u'运营': 'Operations',
    u'活动': 'Event',
    u'拉长': 'Leader',
    u'验证': 'Verification',
    u'业务': 'Business',
    u'热能': 'Energy',
    u'界面': 'UI',
    u'航空': 'Airline',
    u'动物': 'Animal',
    u'技术员': 'Engineer',
    u'培训师': 'Trainers',
    u'射频': 'RF',
    u'文字编辑': 'Copy',
    u'指导': 'Director',
    u'期货': 'Futures',
    u'贸易': 'Trade',
    u'文化': 'Culture',
    u'建筑工程': 'Construction',
    u'规划设计': 'Planning',
    u'开拓': 'Business',
    u'企划': 'Planning',
    u'CNC': 'CNC',
    u'儿科医生': 'Pediatrician',
    u'传媒': 'Media',
    u'互联网': 'Development',
    u'合伙人': 'Partner',
    u'行业': 'Industry',
    ##
    u'医疗': 'Medicine',
    u'器械': 'Equipment',
    u'生物': 'Biotechnology',
    u'制药': 'Pharmaceuticals',
    u'研发': 'R&D',
    u'生产': 'Manufacturing',
    u'质量': 'Quality',
    u'管理': 'Management',
    u'市场': 'Marketing',
    u'总监': 'Director',
    u'销售': 'Sales',
    u'项目': 'Project',
    u'经理': 'Manager',
    u'主管': 'Supervisor',
    u'专员': 'Specialist',
    u'助理': 'Assistant',
    u'质量管理': 'QA',
    u'质量测试': 'QC',
    u'体系': 'Systems',
    u'工程师': 'Engineer',
    u'审核员': 'Auditor',
    u'医药': 'Pharmaceutical',
    u'药品': 'Pharmaceutical',
    u'推广': 'Promotion',
    u'硬件': 'Hardware',
    u'开发': 'Development',
    u'IT' : 'IT',
    u'运维': 'Operation',
    u'技术': 'Technical',
    u'支持': 'Support',
}


def tags_generator(string):
    results = set()
    for word in jieba.cut_for_search(string):
        try:
            results.add(tags[word])
        except KeyError:
            continue
    assert results
    return results
