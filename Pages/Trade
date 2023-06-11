st.subheader("Trade")

st.markdown("<h2 style='text-align: center; color: white;'>Trade Traditional investment instruments, FOREX and Crypto</h2>" , unsafe_allow_html = True)

from ibapi.client import EClient
from ibapi.wrapper import EWrapper


class IBapi(EWrapper , EClient) :
      def __init__(self) :
      EClient.__init__(self , self)

app = IBapi()
app.connect('127.0.0.1' , 7497 , 123)
app.run()

#Uncomment this section if unable to connect
#and to prevent errors on a reconnect
import time
time.sleep(2)
app.disconnect()
''

st.components.v1.iframe("https://trade.ironbeam.com/login" , width = 1111 , height = 700 , scrolling = True)

symbol = st.sidebar.text_input("Symbol" , value = 'MSFT' , max_chars = None , key = None , type = 'default')

