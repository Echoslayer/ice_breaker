import dotenv
import os
from langchain import PromptTemplate
from langchain_openai import ChatOpenAI

if __name__ == "__main__":

    print("Hello, this is the ice breaker script!")

    dotenv.load_dotenv()

    summary_template = """
    given the following information {information} about a person, write a short summary about them.
    1. A short summary
    2. two interesting facts about them
    """

    information = """
伊隆·馬斯克
Elon Musk
Portrait of Elon Musk, a white, middle-age man with short, dark hair, wearing a black suit
2025年的馬斯克
總統高級顧問
兼掌政府效率部
任期
2025年1月20日—2025年5月30日
總統	唐納·川普
前任	職務創立
繼任	職務取消
個人資料
出生	1971年6月28日（53歲）
南非川斯瓦省普勒托利亞
國籍	南非（1971年起）
加拿大（1971年起）
美國（2002年起）
配偶	
賈斯汀·馬斯克
（2000年結婚—2008年離婚）
妲露拉·萊莉
（2010年結婚—2012年離婚）
​（2013年復婚—2016年離婚）
伴侶	格萊姆斯（2018年-2021年）[1]
兒女	14名[2][註 1]
親屬	
托斯卡·馬斯克（妹妹）
金巴爾·馬斯克（弟弟）
林登·里夫（表弟）
母校	
普勒托利亞大學
女王大學（1990年-1992年，轉學）
賓夕法尼亞大學（理學士、文學士）
史丹佛大學（博士班輟學）
職業	
SpaceX 創始人、董事長、執行長、首席工程師
特斯拉執行長、產品設計師、前董事長
Twitter（X）唯一持有者
X公司創始人、董事長
xAI 創始人
Musk Foundation 董事長
無聊公司創始人
Neuralink、OpenAI、Zip2 聯合創始人
簽名	伊隆·馬斯克
2022年的伊隆·馬斯克。	
本條目屬於
伊隆·馬斯克系列
獎項和榮譽 觀點
關聯公司
Zip2 X.com PayPal SpaceX 特斯拉 特斯拉能源 OpenAI Neuralink 無聊公司 X公司 xAI
社群媒體
X（前Twitter）
流行文化
伊隆·馬斯克傳 荒唐 權力遊戲 內部使用 柏拉圖式變奏曲 墜落地球的馬斯克 莫蒂團隊飛躍杜鵑窩
相關條目
鑽洞試驗隧道 特斯拉的爭議 馬斯克家族 超迴路列車 太空特斯拉Roadster TSLAQ 收購推特案 政府效率部
閱論編
伊隆·里夫·馬斯克（英語：Elon Reeve Musk /ˈiːlɔːn/；1971年6月28日—），漢名馬誼郎[註 2]，世界首富、商業大亨、英國皇家學會會士[註 3]、美國工程院院士[6]。他是SpaceX的創始人、董事長、執行長、首席工程師，特斯拉投資人、執行長、產品設計師、前董事長，無聊公司創始人，Neuralink、OpenAI聯合創始人，同時也是X公司的技術長、董事長。2022年馬斯克以2190億美元財富成為世界首富。[7]

馬斯克在南非川斯瓦省普勒托利亞長大，曾短暫就讀於普勒托利亞大學，後於18歲移居加拿大就讀女王大學。兩年後，他轉學到賓夕法尼亞大學，並獲得經濟學、物理學的學士學位。1995年，他搬到加利福尼亞州並就讀於史丹佛大學，而後決定從商。他與弟弟金巴爾共同創辦了網路軟體公司Zip2。1999年，康柏公司以3.07億美元收購了這家初創企業。同年，馬斯克聯合創辦了線上銀行X.com。2000年，該公司與Confinity合併為PayPal。2002年，EBay以15億美元買下PayPal。

2002年，馬斯克創辦SpaceX，並擔任董事長、執行長、技術長，該公司主要負責太空運輸、航太製造。2004年，他加入電動車製造商特斯拉，並擔任董事長與產品設計師，2008年兼任執行長。2006年，他協助創立太陽能服務公司SolarCity，該公司後成為特斯拉子公司特斯拉能源。2015年，他聯合創辦了非營利公司OpenAI，用於研究和推動友善人工智慧。2016年，他聯合創辦了神經科技公司Neuralink，該公司專注於開發人機介面。同年，他成立了無聊隧道施工公司，用於研發超迴路列車。[註 4]2022年10月27日，馬斯克以440億美元收購社群平台Twitter，日後改組為X。2021年10月，美國商業雜誌《富比士》宣布馬斯克財富達到2700億美元，成為該雜誌統計史上最富有的人[8]。2024年11月，美國總統當選人唐納·川普宣布委任馬斯克為總統高級顧問，領導新創立的政府效率部。[9]

馬斯克被認為曾發表一些誤導性或違背科學的言論以及傳播關於COVID-19的錯誤資訊而受到批評。此外，馬斯克在人工智慧、加密貨幣、大眾運輸等方面的觀點亦受到部分專家的批評。
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(
        model="gpt-3.5-turbo-1106",
        temperature=0,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
    )

    chain = summary_prompt_template | llm

    res = chain.invoke(input={"information": information})
    print(res)
