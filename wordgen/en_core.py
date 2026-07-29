# -*- coding: utf-8 -*-
"""Part 1: English core 600 words (8 categories x 75)"""
# Format: word|meaning|phonetic|example_en|example_cn|category|level
en_core = """
inquiry|询盘|ɪnˈkwaɪəri|We received an inquiry from a Russian buyer.|我们收到了俄罗斯买家的询盘。|询盘回复|core
quotation|报价|kwoʊˈteɪʃn|Please send us your quotation by Friday.|请在周五前发送报价。|询盘回复|core
specification|规格|ˌspesɪfɪˈkeɪʃn|The specification meets international standards.|规格符合国际标准。|询盘回复|core
catalog|产品目录|ˈkætəlɔːɡ|Here is our latest product catalog.|这是我们最新的产品目录。|询盘回复|core
brochure|宣传册|broʊˈʃʊr|Could you send me your company brochure?|能发一份公司宣传册吗？|询盘回复|core
sample|样品|ˈsæmpl|We'd like to request a sample for testing.|我们想索取一个样品测试。|询盘回复|core
MOQ|起订量|ˌem oʊˈkjuː|What is your MOQ for this product?|这款产品的起订量是多少？|询盘回复|core
lead time|交货周期|liːd|The lead time is 15-20 days.|交货周期是15-20天。|询盘回复|core
delivery time|交货时间|dɪˈlɪvəri|Delivery time depends on the order quantity.|交货时间取决于订单数量。|询盘回复|core
freight|运费|freɪt|Freight is not included in the unit price.|运费不包含在单价中。|询盘回复|core
packaging|包装|ˈpækɪdʒɪŋ|Custom packaging is available upon request.|可按要求提供定制包装。|询盘回复|core
label|标签|ˈleɪbl|Each product comes with a label.|每件产品都配有标签。|询盘回复|core
brand|品牌|brænd|We are a well-known brand in China.|我们是中国知名品牌。|询盘回复|core
OEM|代工|ˌoʊ iː ˈem|We provide OEM services for overseas clients.|我们为海外客户提供代工服务。|询盘回复|core
ODM|贴牌设计|ˌoʊ diː ˈem|Our ODM team can design products to your needs.|我们的ODM团队可按需设计产品。|询盘回复|core
customization|定制|ˌkʌstəməˈzeɪʃn|We offer full customization for bulk orders.|大宗订单支持全面定制。|询盘回复|core
certificate|证书|sərˈtɪfɪkət|All products come with a quality certificate.|所有产品均附质量证书。|询盘回复|core
compliance|合规|kəmˈplaɪəns|Our factory is in full compliance with EU regulations.|我们工厂完全符合欧盟法规。|询盘回复|core
standard|标准|ˈstændərd|This model meets CE standards.|该型号符合CE标准。|询盘回复|core
quality|质量|ˈkwɑːləti|Quality is our top priority.|质量是我们的首要考虑。|询盘回复|core
grade|等级|ɡreɪd|We offer different grades for different budgets.|我们提供不同等级以适应不同预算。|询盘回复|core
material|材质|məˈtɪriəl|What material is used for the housing?|外壳用的是什么材质？|询盘回复|core
dimension|尺寸|daɪˈmenʃn|Please confirm the dimension before ordering.|下单前请确认尺寸。|询盘回复|core
capacity|容量|kəˈpæsəti|The capacity ranges from 500ml to 2L.|容量从500毫升到2升不等。|询盘回复|core
model|型号|ˈmɑːdl|Which model are you interested in?|您对哪个型号感兴趣？|询盘回复|core
trial order|试订单|ˈtraɪəl|We'd like to place a trial order first.|我们想先下一个试订单。|询盘回复|core
bulk order|大宗订单|bʌlk|We offer discounts for bulk orders.|大宗订单有折扣。|询盘回复|core
repeat order|返单|rɪˈpiːt|Thank you for your repeat order.|感谢您的返单。|询盘回复|core
exclusive|独家|ɪkˈskluːsɪv|We can offer you exclusive rights in your region.|我们可以给您该区域的独家代理权。|询盘回复|core
distributor|经销商|dɪˈstrɪbjətər|We are looking for a distributor in Russia.|我们在寻找俄罗斯的经销商。|询盘回复|core
commission|佣金|kəˈmɪʃn|The agent receives a 5% commission.|代理获得5%的佣金。|询盘回复|core
territory|区域|ˈterətɔːri|Your territory covers all of Eastern Europe.|您的区域覆盖整个东欧。|询盘回复|core
procurement|采购|prəˈkʊrmənt|Our procurement team will review your offer.|我们的采购团队将审核您的报价。|询盘回复|core
sourcing|寻源|ˈsɔːrsɪŋ|We provide sourcing services for foreign buyers.|我们为外国买家提供寻源服务。|询盘回复|core
RFQ|询价单|ˌɑːr ef ˈkjuː|Please submit your RFQ through our website.|请通过我们的网站提交询价单。|询盘回复|core
datasheet|规格书|ˈdeɪtəʃiːt|I've attached the technical datasheet for your reference.|我已附上技术规格书供您参考。|询盘回复|core
prototype|样品|ˈproʊtətaɪp|We can make a prototype within 7 days.|我们可以在7天内制作样品。|询盘回复|core
modification|修改|ˌmɑːdɪfɪˈkeɪʃn|Any modification to the design will take extra time.|设计的任何修改都需要额外时间。|询盘回复|core
approval|批准|əˈpruːvl|We need your approval before mass production.|量产前需要您的批准。|询盘回复|core
confirmation|确认|ˌkɑːnfərˈmeɪʃn|Please send us your written confirmation.|请发送书面确认。|询盘回复|core
origin|原产地|ˈɔːrɪdʒɪn|The certificate of origin will be provided.|将提供原产地证书。|询盘回复|core
warranty|保修|ˈwɔːrənti|We offer a 2-year warranty on all products.|所有产品提供两年保修。|询盘回复|core
after-sales|售后|ˈæftər seɪlz|Our after-sales service is available 24/7.|我们的售后服务全天候可用。|询盘回复|core
maintenance|维护|ˈmeɪntənəns|Regular maintenance extends the product lifespan.|定期维护延长产品寿命。|询盘回复|core
spare parts|备件|sper pɑːrts|Spare parts are available for 5 years.|备件供应保证5年。|询盘回复|core
installation|安装|ˌɪnstəˈleɪʃn|We provide free installation guidance.|我们提供免费安装指导。|询盘回复|core
training|培训|ˈtreɪnɪŋ|On-site training is available for bulk orders.|大宗订单可提供现场培训。|询盘回复|core
technical support|技术支持|ˈteknɪkl|Our technical support team is ready to help.|我们的技术支持团队随时待命。|询盘回复|core
user manual|用户手册|ˈjuːzər|A user manual is included in the package.|包装内附用户手册。|询盘回复|core
FAQ|常见问题|ˌef eɪ ˈkjuː|Please check our FAQ page first.|请先查看我们的常见问题页面。|询盘回复|core
feedback|反馈|ˈfiːdbæk|We value your feedback on our products.|我们重视您对产品的反馈。|询盘回复|core
update|更新|ʌpˈdeɪt|We will keep you updated on the production progress.|我们将随时更新生产进度。|询盘回复|core
follow-up|跟进|ˈfɑːloʊ ʌp|Thank you for your follow-up email.|感谢您的跟进邮件。|询盘回复|core
reply|回复|rɪˈplaɪ|We look forward to your early reply.|期待您的早日回复。|询盘回复|core
prompt|及时的|prɑːmpt|Thank you for your prompt response.|感谢您的及时回复。|询盘回复|core
detail|细节|ˈdiːteɪl|Could you provide more details about the product?|能否提供更多产品细节？|询盘回复|core
requirement|要求|rɪˈkwaɪərmənt|Please let us know your specific requirements.|请告知您的具体要求。|询盘回复|core
preference|偏好|ˈprefrəns|What is your preference for packaging?|您对包装有什么偏好？|询盘回复|core
budget|预算|ˈbʌdʒɪt|What is your target budget for this project?|这个项目的目标预算是多少？|询盘回复|core
target price|目标价|ˈtɑːrɡɪt|Could you share your target price?|能分享一下您的目标价吗？|询盘回复|core
competitive|有竞争力的|kəmˈpetətɪv|Our prices are highly competitive.|我们的价格非常有竞争力。|询盘回复|core
negotiate|谈判|nɪˈɡoʊʃieɪt|We are willing to negotiate on price.|我们愿意就价格进行谈判。|询盘回复|core
favorable|优惠的|ˈfeɪvərəbl|We can offer favorable terms for long-term partners.|我们为长期合作伙伴提供优惠条件。|询盘回复|core
long-term|长期的|lɔːŋ tɜːrm|We seek long-term business relationships.|我们寻求长期商业关系。|询盘回复|core
partnership|合作伙伴关系|ˈpɑːrtnərʃɪp|We value our partnership with your company.|我们重视与贵公司的合作关系。|询盘回复|core
mutual benefit|互利|ˈmjuːtʃuəl|We believe in mutual benefit cooperation.|我们信奉互利合作。|询盘回复|core
trust|信任|trʌst|Trust is the foundation of our business.|信任是我们业务的基础。|询盘回复|core
reliable|可靠的|rɪˈlaɪəbl|We are a reliable supplier with 10 years of experience.|我们是有10年经验的可靠供应商。|询盘回复|core
reputation|声誉|ˌrepjuˈteɪʃn|We have a good reputation in the industry.|我们在行业内有良好声誉。|询盘回复|core
experience|经验|ɪkˈspɪriəns|We have rich experience in export trade.|我们在出口贸易方面经验丰富。|询盘回复|core
professional|专业的|prəˈfeʃənl|Our team is professional and efficient.|我们的团队专业高效。|询盘回复|core
efficient|高效的|ɪˈfɪʃnt|We ensure efficient communication and delivery.|我们确保高效沟通和交付。|询盘回复|core
factory|工厂|ˈfæktəri|Welcome to visit our factory.|欢迎参观我们的工厂。|询盘回复|core
manufacturer|制造商|ˌmænjuˈfæktʃərər|We are a direct manufacturer, not a trading company.|我们是直接制造商，不是贸易公司。|询盘回复|core
exporter|出口商|ɪkˈspɔːrtər|As a leading exporter, we ship worldwide.|作为领先的出口商，我们全球发货。|询盘回复|core
importer|进口商|ɪmˈpɔːrtər|The importer requested a lower price.|进口商要求更低的价格。|询盘回复|core
wholesaler|批发商|ˈhoʊlseɪlər|We supply products to wholesalers across Europe.|我们向全欧洲的批发商供货。|询盘回复|core
retailer|零售商|ˈriːteɪlər|Our products are sold by major retailers.|我们的产品由主要零售商销售。|询盘回复|core
price|价格|praɪs|The price is negotiable for large quantities.|大批量价格可议。|报价谈判|core
unit price|单价|ˈjuːnɪt|The unit price is $25 FOB Shanghai.|单价是25美元FOB上海。|报价谈判|core
FOB|离岸价|fɑːb|We usually quote FOB Shanghai.|我们通常报FOB上海价。|报价谈判|core
CIF|到岸价|sɪf|The CIF price includes insurance and freight.|CIF价包含保险和运费。|报价谈判|core
EXW|出厂价|ˌiː eks ˈdʌbljuː|EXW price means the buyer handles all shipping.|出厂价意味着买方负责所有运输。|报价谈判|core
discount|折扣|ˈdɪskaʊnt|We can offer a 10% discount for orders over 1000 units.|1000件以上订单可享9折优惠。|报价谈判|core
markup|加价|ˈmɑːrkʌp|The retailer's markup is about 30%.|零售商的加价约30%。|报价谈判|core
margin|利润率|ˈmɑːrdʒɪn|Our profit margin is very thin on this product.|这款产品的利润率很薄。|报价谈判|core
profit|利润|ˈprɑːfɪt|We need to maintain a reasonable profit.|我们需要保持合理利润。|报价谈判|core
cost|成本|kɔːst|Raw material costs have risen recently.|原材料成本最近上涨了。|报价谈判|core
offer|报价|ˈɔːfər|This is our best offer for this quarter.|这是本季度我们的最优报价。|报价谈判|core
counteroffer|还价|ˈkaʊntərɔːfər|Your counteroffer is below our cost.|您的还价低于我们的成本。|报价谈判|core
bargain|讨价还价|ˈbɑːrɡɪn|Let's not bargain over small amounts.|我们不要为小额讨价还价了。|报价谈判|core
deal|交易|diːl|It's a deal! We'll proceed with the order.|成交！我们将推进订单。|报价谈判|core
contract|合同|ˈkɑːntrækt|We need to sign a contract before production.|生产前需要签合同。|报价谈判|core
terms|条款|tɜːrmz|Let's discuss the terms of payment.|让我们讨论付款条款。|报价谈判|core
condition|条件|kənˈdɪʃn|Under what conditions can you lower the price?|什么条件下您可以降价？|报价谈判|core
deposit|定金|ˈdɑːpɑːzɪt|A 30% deposit is required before production.|生产前需要30%定金。|报价谈判|core
balance|尾款|ˈbæləns|The balance should be paid before shipment.|尾款应在发货前付清。|报价谈判|core
payment|付款|ˈpeɪmənt|What are your payment terms?|你们的付款条件是什么？|报价谈判|core
currency|货币|ˈkɜːrənsi|We accept payment in USD or EUR.|我们接受美元或欧元付款。|报价谈判|core
exchange rate|汇率|ɪksˈtʃeɪndʒ|The exchange rate affects our pricing.|汇率影响我们的定价。|报价谈判|core
invoice|发票|ˈɪnvɔɪs|We will send the proforma invoice today.|我们今天会发送形式发票。|报价谈判|core
receipt|收据|rɪˈsiːt|Please keep the payment receipt for your records.|请保留付款收据备查。|报价谈判|core
refund|退款|ˈriːfʌnd|We will process the refund within 5 days.|我们将在5天内处理退款。|报价谈判|core
adjustment|调整|əˈdʒʌstmənt|We need a price adjustment due to rising costs.|因成本上升我们需要调整价格。|报价谈判|core
revision|修订|rɪˈvɪʒn|Please review the revision and confirm.|请审核修订并确认。|报价谈判|core
valid|有效的|ˈvælɪd|This quotation is valid for 30 days.|此报价有效期为30天。|报价谈判|core
expire|到期|ɪkˈspaɪər|The offer will expire at the end of this month.|报价将于本月底到期。|报价谈判|core
minimum|最低的|ˈmɪnɪməm|The minimum order value is $5000.|最低订单金额为5000美元。|报价谈判|core
maximum|最高的|ˈmæksɪməm|The maximum discount we can offer is 15%.|我们能提供的最大折扣是15%。|报价谈判|core
range|范围|reɪndʒ|The price range is from $10 to $50.|价格范围从10到50美元。|报价谈判|core
quote|报价|kwoʊt|Let me quote you our best price.|让我给您报最优价格。|报价谈判|core
estimate|估算|ˈestɪmeɪt|Can you give me a rough estimate?|能给我一个粗略估算吗？|报价谈判|core
calculate|计算|ˈkælkjuleɪt|Let me calculate the total cost for you.|让我为您计算总成本。|报价谈判|core
total|总计|ˈtoʊtl|The total amount is $15,000.|总金额为15000美元。|报价谈判|core
subtotal|小计|ˈsʌbtoʊtl|The subtotal before tax is $12,000.|税前小计为12000美元。|报价谈判|core
additional|额外的|əˈdɪʃənl|Are there any additional charges?|有额外费用吗？|报价谈判|core
hidden cost|隐性成本|ˈhɪdn|There are no hidden costs in our quotation.|我们的报价中没有隐性成本。|报价谈判|core
transparent|透明的|trænsˈpærənt|Our pricing is fully transparent.|我们的定价完全透明。|报价谈判|core
fair|公平的|fer|We believe this is a fair price for both sides.|我们相信这对双方都是公平价格。|报价谈判|core
reasonable|合理的|ˈriːzənəbl|The price is reasonable considering the quality.|考虑到质量，价格是合理的。|报价谈判|core
acceptable|可接受的|əkˈseptəbl|Is the price acceptable to you?|这个价格您可以接受吗？|报价谈判|core
reject|拒绝|rɪˈdʒekt|We have to reject this offer as it's too low.|我们不得不拒绝这个报价，太低了。|报价谈判|core
accept|接受|əkˈsept|We accept your offer and will proceed.|我们接受您的报价并将继续推进。|报价谈判|core
confirm|确认|kənˈfɜːrm|Please confirm the order details by email.|请通过邮件确认订单细节。|报价谈判|core
sign|签署|saɪn|Both parties need to sign the agreement.|双方需要签署协议。|报价谈判|core
agree|同意|əˈɡriː|Do you agree with the proposed terms?|您同意提议的条款吗？|报价谈判|core
disagree|不同意|ˌdɪsəˈɡriː|We disagree with the delivery schedule.|我们不同意交货时间表。|报价谈判|core
compromise|妥协|ˈkɑːmprəmaɪz|Let's find a compromise that works for both.|让我们找到一个双方都能接受的折中方案。|报价谈判|core
concession|让步|kənˈseʃn|We can make a concession on the payment terms.|我们可以在付款条件上做出让步。|报价谈判|core
final|最终的|ˈfaɪnl|This is our final offer.|这是我们的最终报价。|报价谈判|core
conclude|达成|kənˈkluːd|We are glad to conclude this deal.|我们很高兴达成这笔交易。|报价谈判|core
shipping|运输|ˈʃɪpɪŋ|Shipping arrangements will be made next week.|运输安排将在下周进行。|物流交货|core
logistics|物流|ləˈdʒɪstɪks|Our logistics partner ensures timely delivery.|我们的物流合作伙伴确保及时交付。|物流交货|core
forwarder|货代|ˈfɔːrwərdər|Please contact our forwarder for shipping details.|请联系我们的货代了解运输细节。|物流交货|core
carrier|承运人|ˈkæriər|The carrier will pick up the goods tomorrow.|承运人明天来提货。|物流交货|core
vessel|船只|ˈvesl|The vessel departs from Shanghai on Monday.|船只周一从上海出发。|物流交货|core
container|集装箱|kənˈteɪnər|We need a 20-foot container for this order.|这批订单需要一个20尺柜。|物流交货|core
LCL|拼箱|ˌel siː ˈel|For small orders, we can arrange LCL shipping.|小订单我们可以安排拼箱运输。|物流交货|core
FCL|整箱|ˌef siː ˈel|FCL shipping is more cost-effective for bulk orders.|整箱运输对大宗订单更经济。|物流交货|core
port|港口|pɔːrt|The nearest port is Shanghai Port.|最近的港口是上海港。|物流交货|core
terminal|码头|ˈtɜːrmɪnl|The cargo has arrived at the terminal.|货物已到达码头。|物流交货|core
customs|海关|ˈkʌstəmz|The goods are awaiting customs clearance.|货物正在等待清关。|物流交货|core
clearance|清关|ˈklɪrəns|Customs clearance usually takes 2-3 days.|清关通常需要2-3天。|物流交货|core
declaration|申报|ˌdekləˈreɪʃn|Please prepare the customs declaration form.|请准备海关申报单。|物流交货|core
tariff|关税|ˈtærɪf|The import tariff is 5% for this category.|该类别的进口关税为5%。|物流交货|core
duty|关税|ˈduːti|Import duties must be paid before release.|进口关税必须在放行前支付。|物流交货|core
inspection|检验|ɪnˈspekʃn|The goods passed quality inspection.|货物通过了质量检验。|物流交货|core
bill of lading|提单|bɪl əv ˈleɪdɪŋ|The bill of lading will be issued after shipment.|提单将在发货后出具。|物流交货|core
tracking|追踪|ˈtrækɪŋ|You can track your shipment online.|您可以在线追踪货物。|物流交货|core
ETA|预计到货|ˌiː tiː ˈeɪ|The ETA is August 15th.|预计到货时间是8月15日。|物流交货|core
delivery|交付|dɪˈlɪvəri|Delivery will be made to your warehouse.|货物将交付到您的仓库。|物流交货|core
dispatch|发货|dɪˈspætʃ|We will dispatch the goods upon receiving payment.|收到付款后我们将发货。|物流交货|core
pickup|提货|ˈpɪkʌp|The pickup is scheduled for tomorrow morning.|提货安排在明天上午。|物流交货|core
loading|装货|ˈloʊdɪŋ|Loading will be completed by 5 PM.|装货将在下午5点前完成。|物流交货|core
unloading|卸货|ʌnˈloʊdɪŋ|Unloading at the destination takes about 2 hours.|目的港卸货约需2小时。|物流交货|core
transit|运输中|ˈtrænzɪt|Your goods are in transit.|您的货物正在运输中。|物流交货|core
delay|延误|dɪˈleɪ|We apologize for the delay in shipment.|我们对发货延误表示歉意。|物流交货|core
schedule|时间表|ˈskedʒuːl|The shipping schedule has been confirmed.|运输时间表已确认。|物流交货|core
deadline|截止日期|ˈdedlaɪn|We must meet the delivery deadline.|我们必须赶上交货截止日期。|物流交货|core
urgent|紧急的|ˈɜːrdʒənt|This is an urgent shipment that needs air freight.|这是一批需要空运的紧急货物。|物流交货|core
air freight|空运|er freɪt|Air freight is faster but more expensive.|空运更快但更贵。|物流交货|core
sea freight|海运|siː freɪt|Sea freight is the most economical option.|海运是最经济的选择。|物流交货|core
land transport|陆运|lænd ˈtrænspɔːrt|Land transport is suitable for neighboring countries.|陆运适合邻国运输。|物流交货|core
railway|铁路|ˈreɪlweɪ|Railway transport is a good alternative to sea freight.|铁路运输是海运的好替代方案。|物流交货|core
warehouse|仓库|ˈwerhaʊs|The goods are stored in our warehouse.|货物存放在我们的仓库。|物流交货|core
storage|存储|ˈstɔːrɪdʒ|Storage fees apply if goods are not picked up on time.|如未按时提货将产生仓储费。|物流交货|core
inventory|库存|ˈɪnvəntɔːri|We maintain sufficient inventory for fast delivery.|我们保持充足库存以快速交付。|物流交货|core
stock|库存|stɑːk|The item is currently out of stock.|该商品目前缺货。|物流交货|core
shortage|短缺|ˈʃɔːrtɪdʒ|There is a shortage of shipping containers.|目前集装箱短缺。|物流交货|core
damage|损坏|ˈdæmɪdʒ|Please check for any damage upon receipt.|收货时请检查是否有损坏。|物流交货|core
loss|丢失|lɔːs|We will file a claim for the lost shipment.|我们将为丢失的货物提出索赔。|物流交货|core
insurance|保险|ɪnˈʃʊrəns|Marine insurance covers transit risks.|海运保险覆盖运输风险。|物流交货|core
claim|索赔|kleɪm|We submitted a claim for the damaged goods.|我们为损坏的货物提交了索赔。|物流交货|core
compensation|赔偿|ˌkɑːmpenˈseɪʃn|We will offer compensation for the delay.|我们将为延误提供赔偿。|物流交货|core
risk|风险|rɪsk|Who bears the risk during transit?|运输期间风险由谁承担？|物流交货|core
responsibility|责任|rɪˌspɑːnsəˈbɪləti|It's our responsibility to deliver on time.|按时交付是我们的责任。|物流交货|core
coordinate|协调|koʊˈɔːrdɪneɪt|We will coordinate with the forwarder.|我们将与货代协调。|物流交货|core
arrange|安排|əˈreɪndʒ|We can arrange door-to-door delivery.|我们可以安排门到门配送。|物流交货|core
notify|通知|ˈnoʊtɪfaɪ|We will notify you once the goods are shipped.|货物发出后我们会通知您。|物流交货|core
destination|目的地|ˌdestɪˈneɪʃn|What is the final destination port?|最终目的港是哪里？|物流交货|core
route|路线|ruːt|We chose the fastest shipping route.|我们选择了最快的运输路线。|物流交货|core
distance|距离|ˈdɪstəns|The distance affects the shipping cost.|距离影响运输成本。|物流交货|core
weight|重量|weɪt|The gross weight is 500 kg.|毛重500公斤。|物流交货|core
volume|体积|ˈvɑːljuːm|Please provide the volume of the shipment.|请提供货物的体积。|物流交货|core
measurement|尺寸|ˈmeʒərmənt|The measurement of each carton is 50x40x30 cm.|每个纸箱的尺寸是50x40x30厘米。|物流交货|core
pallet|托盘|ˈpælət|The goods are packed on pallets.|货物打包在托盘上。|物流交货|core
carton|纸箱|ˈkɑːrtn|Each carton contains 24 units.|每个纸箱装24件。|物流交货|core
package|包裹|ˈpækɪdʒ|The package has been sent out.|包裹已发出。|物流交货|core
fragile|易碎的|ˈfrædʒl|Fragile goods need special packaging.|易碎品需要特殊包装。|物流交货|core
T/T|电汇|ˌtiː ˈtiː|We accept payment by T/T.|我们接受电汇付款。|支付结算|core
L/C|信用证|ˌel ˈsiː|For large orders, we require an L/C.|大订单我们要求信用证付款。|支付结算|core
PayPal|贝宝|ˈpeɪpæl|Small orders can be paid via PayPal.|小订单可通过PayPal付款。|支付结算|core
advance payment|预付款|ədˈvæns|A 30% advance payment is required.|需要30%预付款。|支付结算|core
down payment|首付款|daʊn|The down payment is due before production starts.|首付款应在生产开始前支付。|支付结算|core
installment|分期付款|ɪnˈstɔːrlmənt|We accept payment in three installments.|我们接受分三期付款。|支付结算|core
full payment|全款|fʊl|Full payment is required for small orders.|小订单需全款支付。|支付结算|core
outstanding|未付的|aʊtˈstændɪŋ|You have an outstanding balance of $5000.|您有5000美元未付余额。|支付结算|core
overdue|逾期的|ˌoʊvərˈduː|The payment is 15 days overdue.|付款已逾期15天。|支付结算|core
settle|结清|ˈsetl|Please settle the account within 30 days.|请在30天内结清账目。|支付结算|core
remit|汇款|rɪˈmɪt|Please remit the payment to our bank account.|请将款项汇至我们的银行账户。|支付结算|core
transfer|转账|trænsˈfɜːr|Bank transfer usually takes 2-3 working days.|银行转账通常需要2-3个工作日。|支付结算|core
bank account|银行账户|bæŋk|Please make the payment to our bank account.|请将款项付至我们的银行账户。|支付结算|core
account number|账号|əˈkaʊnt|Please confirm our account number before transfer.|转账前请确认我们的账号。|支付结算|core
SWIFT code|SWIFT代码|swɪft|You will need our SWIFT code for international transfers.|国际汇款需要我们的SWIFT代码。|支付结算|core
beneficiary|收款人|ˌbenɪˈfɪʃieri|The beneficiary name must match exactly.|收款人名称必须完全一致。|支付结算|core
bank charges|银行手续费|bæŋk|Bank charges are not included in the price.|价格不包含银行手续费。|支付结算|core
transaction|交易|trænˈzækʃn|Each transaction is recorded in our system.|每笔交易都记录在我们的系统中。|支付结算|core
voucher|凭证|ˈvaʊtʃər|Please keep the payment voucher for your records.|请保留付款凭证备查。|支付结算|core
statement|对账单|ˈsteɪtmənt|We will send you a monthly statement.|我们将发送月度对账单。|支付结算|core
reconcile|对账|ˈrekənsaɪl|Let's reconcile the accounts at the end of the month.|让我们在月底对账。|支付结算|core
discrepancy|差异|dɪsˈkrepənsi|There is a discrepancy in the invoice amount.|发票金额有差异。|支付结算|core
credit note|贷记单|ˈkredɪt|We will issue a credit note for the returned goods.|我们将为退货开具贷记单。|支付结算|core
deduction|扣款|dɪˈdʌkʃn|We made a deduction for the damaged items.|我们对损坏物品进行了扣款。|支付结算|core
penalty|罚款|ˈpenəlti|A late payment penalty of 0.5% per day applies.|逾期付款每天罚款0.5%。|支付结算|core
fluctuation|波动|ˌflʌktʃuˈeɪʃn|Exchange rate fluctuations affect our profit.|汇率波动影响我们的利润。|支付结算|core
guarantee|保证|ˌɡærənˈtiː|We guarantee the quality of our products.|我们保证产品质量。|支付结算|core
verify|核实|ˈverɪfaɪ|Please verify the payment details before transfer.|转账前请核实付款信息。|支付结算|core
document|文件|ˈdɑːkjumənt|All payment documents must be kept on file.|所有付款文件必须存档。|支付结算|core
attach|附上|əˈtætʃ|Please attach the payment proof to your email.|请在邮件中附上付款证明。|支付结算|core
proof|证明|pruːf|We need proof of payment to process the order.|我们需要付款证明才能处理订单。|支付结算|core
process|处理|ˈprɑːses|Your payment is being processed.|您的付款正在处理中。|支付结算|core
pending|待处理的|ˈpendɪŋ|The payment is still pending.|付款仍在处理中。|支付结算|core
complete|完成的|kəmˈpliːt|The transaction has been completed successfully.|交易已成功完成。|支付结算|core
cancel|取消|ˈkænsl|We had to cancel the order due to non-payment.|因未付款我们不得不取消订单。|支付结算|core
agreement|协议|əˈɡriːmənt|Both parties signed the agreement.|双方签署了协议。|合同条款|core
clause|条款|klɔːz|Please review each clause carefully.|请仔细审阅每一条款。|合同条款|core
term|条款|tɜːrm|The terms are negotiable before signing.|签约前条款可协商。|合同条款|core
obligation|义务|ˌɑːblɪˈɡeɪʃn|Each party has its own obligations.|各方都有各自的义务。|合同条款|core
liability|责任|ˌlaɪəˈbɪləti|The seller's liability is limited to the product value.|卖方责任以产品价值为限。|合同条款|core
breach|违约|briːtʃ|A breach of contract has serious consequences.|违约会有严重后果。|合同条款|core
terminate|终止|ˈtɜːrmɪneɪt|Either party can terminate the contract with 30 days notice.|任何一方可提前30天通知终止合同。|合同条款|core
amend|修改|əˈmend|We need to amend clause 5 of the contract.|我们需要修改合同第5条。|合同条款|core
execute|执行|ˈeksɪkjuːt|The contract will be executed upon signature.|合同签署后即生效。|合同条款|core
effective|生效的|ɪˈfektɪv|The agreement becomes effective immediately.|协议立即生效。|合同条款|core
valid|有效的|ˈvælɪd|The contract is valid for one year.|合同有效期为一年。|合同条款|core
expire|到期|ɪkˈspaɪər|The contract expires on December 31st.|合同12月31日到期。|合同条款|core
renew|续约|rɪˈnuː|We'd like to renew the contract for another year.|我们想续约一年。|合同条款|core
extend|延长|ɪkˈstend|Can we extend the delivery period by two weeks?|交货期可以延长两周吗？|合同条款|core
party|当事方|ˈpɑːrti|Both parties agree to the following terms.|双方同意以下条款。|合同条款|core
seller|卖方|ˈselər|The seller is responsible for packaging.|卖方负责包装。|合同条款|core
buyer|买方|ˈbaɪər|The buyer must inspect the goods upon arrival.|买方必须在到货后验货。|合同条款|core
signatory|签署人|ˈsɪgnətɔːri|The authorized signatory must sign the contract.|授权签署人必须签署合同。|合同条款|core
seal|盖章|siːl|Please affix your company seal here.|请在此处加盖公司印章。|合同条款|core
original|原件|əˈrɪdʒənl|We need two original copies of the contract.|我们需要两份合同原件。|合同条款|core
copy|副本|ˈkɑːpi|Please keep a copy for your records.|请保留一份副本备查。|合同条款|core
appendix|附录|əˈpendɪks|The specifications are in Appendix A.|规格详见附录A。|合同条款|core
attachment|附件|əˈtætʃmənt|Please refer to the attachment for details.|详情请参考附件。|合同条款|core
confidential|保密的|ˌkɑːnfɪˈdenʃl|This agreement is strictly confidential.|本协议严格保密。|合同条款|core
exclusive|排他的|ɪkˈskluːsɪv|This is an exclusive distribution agreement.|这是独家经销协议。|合同条款|core
intellectual property|知识产权|ˌɪntəˈlektʃuəl|Our intellectual property is protected by law.|我们的知识产权受法律保护。|合同条款|core
patent|专利|ˈpætnt|The product is protected by a patent.|产品受专利保护。|合同条款|core
trademark|商标|ˈtreɪdmɑːrk|The trademark is registered in 30 countries.|商标在30个国家注册。|合同条款|core
license|许可|ˈlaɪsns|We grant you a license to sell our products.|我们授予您销售我们产品的许可。|合同条款|core
indemnify|赔偿|ɪnˈdemnɪfaɪ|The seller shall indemnify the buyer against claims.|卖方应赔偿买方免受索赔。|合同条款|core
arbitration|仲裁|ˌɑːrbɪˈtreɪʃn|Disputes will be settled through arbitration.|争议将通过仲裁解决。|合同条款|core
jurisdiction|管辖权|ˌdʒʊrɪsˈdɪkʃn|The contract is under Chinese jurisdiction.|合同受中国法律管辖。|合同条款|core
dispute|争议|dɪˈspjuːt|We hope to resolve the dispute amicably.|我们希望能友好解决争议。|合同条款|core
resolve|解决|rɪˈzɑːlv|We will resolve the issue as soon as possible.|我们将尽快解决问题。|合同条款|core
mediation|调解|ˌmiːdiˈeɪʃn|Mediation is cheaper than going to court.|调解比上法庭更经济。|合同条款|core
legal|法律的|ˈliːɡl|Please consult your legal advisor.|请咨询您的法律顾问。|合同条款|core
attorney|律师|əˈtɜːrni|Our attorney will review the contract.|我们的律师将审查合同。|合同条款|core
complaint|投诉|kəmˈpleɪnt|We received a complaint about the product quality.|我们收到了关于产品质量的投诉。|售后投诉|core
defective|有缺陷的|dɪˈfektɪv|Some units were found to be defective.|发现部分产品有缺陷。|售后投诉|core
faulty|有故障的|ˈfɔːlti|The faulty products will be replaced free of charge.|故障产品将免费更换。|售后投诉|core
malfunction|故障|mælˈfʌŋkʃn|The malfunction was caused by improper use.|故障是由不当使用引起的。|售后投诉|core
return|退货|rɪˈtɜːrn|We accept returns within 30 days of purchase.|我们接受购买后30天内退货。|售后投诉|core
exchange|换货|ɪksˈtʃeɪndʒ|We offer free exchange for defective items.|缺陷产品免费换货。|售后投诉|core
replace|更换|rɪˈpleɪs|We will replace the damaged items at no cost.|我们将免费更换损坏的产品。|售后投诉|core
repair|维修|rɪˈper|We can repair the product at our service center.|我们可以在服务中心维修产品。|售后投诉|core
refund|退款|ˈriːfʌnd|We will process a full refund for the returned goods.|我们将为退货全额退款。|售后投诉|core
apologize|道歉|əˈpɑːlədʒaɪz|We sincerely apologize for the inconvenience.|我们对不便表示诚挚道歉。|售后投诉|core
issue|问题|ˈɪʃuː|We are working to resolve the issue.|我们正在努力解决问题。|售后投诉|core
problem|问题|ˈprɑːbləm|What seems to be the problem?|出了什么问题？|售后投诉|core
solution|解决方案|səˈluːʃn|We have a solution for your problem.|我们有一个解决方案。|售后投诉|core
handle|处理|ˈhændl|We will handle this matter personally.|我们将亲自处理此事。|售后投诉|core
investigate|调查|ɪnˈvestɪɡeɪt|We will investigate the cause of the problem.|我们将调查问题原因。|售后投诉|core
cause|原因|kɔːz|What was the cause of the delay?|延误的原因是什么？|售后投诉|core
responsible|负责的|rɪˈspɑːnsəbl|We are responsible for the quality issue.|我们对质量问题负责。|售后投诉|core
understand|理解|ˌʌndərˈstænd|We understand your frustration.|我们理解您的不满。|售后投诉|core
satisfactory|令人满意的|ˌsætɪsˈfæktəri|We hope this solution is satisfactory.|我们希望这个解决方案令您满意。|售后投诉|core
satisfied|满意的|ˈsætɪsfaɪd|Are you satisfied with the resolution?|您对解决方案满意吗？|售后投诉|core
quality issue|质量问题|ˈkwɑːləti|We take every quality issue seriously.|我们认真对待每个质量问题。|售后投诉|core
defect|缺陷|ˈdiːfekt|Please send photos of the defect.|请发送缺陷部位的照片。|售后投诉|core
damage|损坏|ˈdæmɪdʒ|The damage occurred during transit.|损坏发生在运输过程中。|售后投诉|core
broken|破损的|ˈbroʊkən|The item arrived broken.|物品到达时已破损。|售后投诉|core
missing|缺失的|ˈmɪsɪŋ|Some parts are missing from the package.|包裹中缺少部分零件。|售后投诉|core
wrong|错误的|rɔːŋ|We received the wrong model.|我们收到了错误的型号。|售后投诉|core
incorrect|不正确的|ˌɪnkəˈrekt|The quantity is incorrect on the invoice.|发票上的数量不正确。|售后投诉|core
shortage|短缺|ˈʃɔːrtɪdʒ|We found a shortage of 10 units.|我们发现少了10件。|售后投诉|core
delay|延误|dɪˈleɪ|We apologize for the delay in response.|我们为回复延误道歉。|售后投诉|core
improve|改进|ɪmˈpruːv|We will improve our quality control process.|我们将改进质量控制流程。|售后投诉|core
prevent|预防|prɪˈvent|We will prevent this from happening again.|我们将防止此类问题再次发生。|售后投诉|core
quality control|质量控制|ˈkwɑːləti|Our quality control team checks every product.|我们的质检团队检查每件产品。|售后投诉|core
test|测试|test|All products are tested before shipment.|所有产品发货前都经过测试。|售后投诉|core
meeting|会议|ˈmiːtɪŋ|Let's schedule a meeting to discuss the details.|我们安排个会议讨论细节。|商务会议|core
agenda|议程|əˈdʒendə|Here is the agenda for today's meeting.|这是今天会议的议程。|商务会议|core
schedule|安排|ˈskedʒuːl|The meeting is scheduled for 2 PM.|会议安排在下午2点。|商务会议|core
attend|参加|əˈtend|Who will attend the meeting from your side?|贵方谁将参加会议？|商务会议|core
participant|参与者|pɑːrˈtɪsɪpənt|All participants should arrive on time.|所有参与者应准时到达。|商务会议|core
minute|会议纪要|ˈmɪnɪt|Someone should take the meeting minutes.|需要有人做会议纪要。|商务会议|core
presentation|演示|ˌpriːzenˈteɪʃn|The sales presentation was very impressive.|销售演示令人印象深刻。|商务会议|core
discuss|讨论|dɪˈskʌs|Let's discuss the proposal in detail.|让我们详细讨论提案。|商务会议|core
topic|主题|ˈtɑːpɪk|The next topic on the agenda is pricing.|议程的下一个主题是定价。|商务会议|core
point|要点|pɔɪnt|That's a very good point.|这是一个很好的观点。|商务会议|core
question|问题|ˈkwestʃən|Does anyone have any questions?|有人有问题吗？|商务会议|core
answer|回答|ˈænsər|Let me answer your question.|让我回答您的问题。|商务会议|core
suggest|建议|səˈdʒest|May I suggest an alternative approach?|我可以建议一个替代方案吗？|商务会议|core
proposal|提案|prəˈpoʊzl|We reviewed your proposal and have some feedback.|我们审阅了您的提案并有反馈。|商务会议|core
recommend|推荐|ˌrekəˈmend|I recommend we proceed with Plan A.|我建议我们继续方案A。|商务会议|core
opinion|观点|əˈpɪnjən|What's your opinion on this matter?|您对此事有什么看法？|商务会议|core
agree|同意|əˈɡriː|I agree with the proposed strategy.|我同意提议的战略。|商务会议|core
consensus|共识|kənˈsensəs|We reached a consensus on the pricing strategy.|我们在定价策略上达成了共识。|商务会议|core
decision|决定|dɪˈsɪʒn|The final decision will be made by the board.|最终决定将由董事会做出。|商务会议|core
summarize|总结|ˈsʌməraɪz|Let me summarize the key points.|让我总结要点。|商务会议|core
review|回顾|rɪˈvjuː|Let's review what we've discussed today.|让我们回顾今天讨论的内容。|商务会议|core
action item|行动项|ˈækʃn|Each action item has a deadline.|每个行动项都有截止日期。|商务会议|core
follow up|跟进|ˈfɑːloʊ|I'll follow up with the team next week.|我下周会和团队跟进。|商务会议|core
assign|分配|əˈsaɪn|Tasks were assigned to each team member.|任务分配给了每个团队成员。|商务会议|core
deadline|截止日期|ˈdedlaɪn|The deadline for this task is Friday.|这个任务的截止日期是周五。|商务会议|core
priority|优先级|praɪˈɔːrəti|This project is our top priority.|这个项目是我们的首要任务。|商务会议|core
postpone|推迟|poʊstˈpoʊn|We need to postpone the meeting to next week.|我们需要把会议推迟到下周。|商务会议|core
reschedule|重新安排|riːˈskedʒuːl|Can we reschedule the meeting?|我们可以重新安排会议时间吗？|商务会议|core
conference room|会议室|ˈkɑːnfərəns|The conference room is booked for 3 PM.|会议室预订了下午3点。|商务会议|core
video call|视频通话|ˈvɪdioʊ|Let's have a video call to discuss this.|我们开个视频通话讨论一下。|商务会议|core
email|邮件|ˈiːmeɪl|Please send me the details by email.|请通过邮件发送细节。|日常邮件|core
subject|主题|ˈsʌbdʒɪkt|The email subject should be clear and concise.|邮件主题应清晰简洁。|日常邮件|core
attachment|附件|əˈtætʃmənt|Please find the attachment for your reference.|请查收附件供参考。|日常邮件|core
CC|抄送|ˌsiː ˈsiː|Please CC your manager on this email.|请在邮件中抄送您的经理。|日常邮件|core
reply|回复|rɪˈplaɪ|Please reply at your earliest convenience.|请尽快回复。|日常邮件|core
forward|转发|ˈfɔːrwərd|I'll forward the email to the team.|我会把邮件转发给团队。|日常邮件|core
draft|草稿|dræft|I'm still working on the draft.|我还在写草稿。|日常邮件|core
send|发送|send|I'll send the email right away.|我马上发送邮件。|日常邮件|core
receive|收到|rɪˈsiːv|Did you receive my email?|您收到我的邮件了吗？|日常邮件|core
attach|附上|əˈtætʃ|I've attached the file as requested.|我已按要求附上文件。|日常邮件|core
regards|致敬|rɪˈɡɑːrdz|Best regards, Li Xiaoxiao.|此致敬礼，李笑笑。|日常邮件|core
dear|尊敬的|dɪr|Dear Mr. Ivanov, thank you for your inquiry.|尊敬的伊万诺夫先生，感谢您的询盘。|日常邮件|core
thanks|感谢|θæŋks|Thanks for your quick response.|感谢您的快速回复。|日常邮件|core
appreciate|感谢|əˈpriːʃieɪt|We appreciate your support.|感谢您的支持。|日常邮件|core
please|请|pliːz|Please let us know your decision.|请告知您的决定。|日常邮件|core
regarding|关于|rɪˈɡɑːrdɪŋ|I'm writing regarding your order status.|我写信是关于您的订单状态。|日常邮件|core
as per|按照|æz pɜːr|As per our agreement, the delivery is on schedule.|按照我们的协议，交货按计划进行。|日常邮件|core
as discussed|按讨论|dɪˈskʌst|As discussed, please find the revised quotation.|按讨论内容，请查收修订后的报价。|日常邮件|core
for your reference|供参考|ˈrefrəns|The file is attached for your reference.|附件供您参考。|日常邮件|core
on behalf of|代表|bɪˈhæf|On behalf of our company, I thank you.|我代表我们公司感谢您。|日常邮件|core
look forward to|期待|ˈfɔːrwərd|We look forward to your reply.|期待您的回复。|日常邮件|core
in advance|提前|ədˈvæns|Thank you in advance for your cooperation.|提前感谢您的配合。|日常邮件|core
feel free to|随时|friː|Feel free to contact us if you have questions.|如有问题随时联系我们。|日常邮件|core
however|然而|haʊˈevər|The price is competitive, however, MOQ applies.|价格有竞争力，但需满足起订量。|日常邮件|core
therefore|因此|ˈðerfɔːr|Therefore, we request a 30% deposit.|因此，我们要求30%定金。|日常邮件|core
furthermore|此外|ˈfɜːrðərmɔːr|Furthermore, we offer free shipping for orders over $5000.|此外，5000美元以上订单免运费。|日常邮件|core
in addition|此外|əˈdɪʃn|In addition, we provide a 2-year warranty.|此外，我们提供两年保修。|日常邮件|core
due to|由于|duː|The delay was due to customs inspection.|延误是由于海关检查。|日常邮件|core
although|虽然|ɔːlˈðoʊ|Although the price is higher, the quality is superior.|虽然价格更高，但质量更优。|日常邮件|core
despite|尽管|dɪˈspaɪt|Despite the challenges, we met the deadline.|尽管有挑战，我们还是赶上了截止日期。|日常邮件|core
"""
