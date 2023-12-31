import streamlit as st
import time
from PIL import Image

st.title('Streamlit 超入門')
st.write('プログレスバーの表示')

'Start'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.05)

'Done!!!'

image = Image.open('IMG_5314.jpg')

left_column, right_column = st.columns(2)
button = left_column.button('画像を表示')
if button:
    right_column.write(st.image(image, use_column_width=True, caption='The picture of Wimbledon'))

expander = st.expander('問い合わせ')
expander.write('問い合わせの回答')
# text = st.text_input('あなたの趣味を教えてください')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味：', text
# 'コンディション：', condition




#if st.checkbox('Show Image'):
#    img = Image.open('IMG_5314.jpg')
#    st.image(img, caption='London view', use_column_width=True)