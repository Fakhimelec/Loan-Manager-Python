import pandas as pd

from PIL import Image, ImageDraw, ImageFont                           # Pillow Module To Create And Design Image Of Bills
import arabic_reshaper                                              # Used To Make Us Able To Put Persian Text On Image
from bidi.algorithm import get_display                               # Used To Change Persian Letters In Backward Order

import os                                                            # Used To Create A New Folder For Payment
####################################################################################################
# Initiate Variables
####################################################################################################
# َA4 Paper Size = 210 * 297
a4_w = 210
a4_h = 297
scale_factor = 10
img_w = a4_w * scale_factor
img_h = a4_h * scale_factor

####################################################################################################
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
# New Class For Calculating Monthly Payments Prompt Window
#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
class ListPrint:
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def __init__(self):
        super().__init__()
        
        
    def printList(self, Payment_List, Current_Year, Current_Month):
        self.list = Payment_List
        self.year = Current_Year
        self.month = Current_Month
        
        try:
            row = self.list.shape[0]
            if (row != 0):
                
                bill_count = row
                bills_on_page = 8

                # Format Of Inline If
                # expression_if_true if condition else expression_if_false
                paper_count = row//bills_on_page if row%bills_on_page==0 else (row//bills_on_page) + 1
                paper_index = 0
                paragraph_index = 0
                
                for bill_index in range(0, bill_count):
                    
                    if (bill_index%bills_on_page == 0):
                        # Create a new image
                        img = Image.new('RGB', (img_w, img_h), color='white')
                        
                        # Create a drawing context
                        draw = ImageDraw.Draw(img)
                        
                        # Kargahin Laptopi
                        #font_title = ImageFont.truetype(r"Titr Bold.TTF", size=40, encoding='unic')
                        #font_header = ImageFont.truetype(r"Zar.TTF", size=40, encoding='unic')
                        # Evin Laptopi
                        font_title = ImageFont.truetype(r"C:\Users\babak\AppData\Local\Microsoft\Windows\Fonts\TITRB.TTF", size=40, encoding='unic')
                        font_content = ImageFont.truetype(r"C:\Users\babak\AppData\Local\Microsoft\Windows\Fonts\ZAR.TTF", size=45, encoding='unic')
                        

                        # Calculating Center Of The Page
                        horizontal_center = img.width // 2
                        vertical_center = img.height // 2
                        horizontal_ofset = img.width // 2
                        vertical_ofset = img.height // (bills_on_page // 2)
                        top_margin = 80
                        left_margin = 60
                        # Draw A Vertical line On Page Horizontal Center
                        draw.line([(img.width//2, 0), (img.width//2, img.height)], fill ="Black", width = 5)
                        
                    # Set The Title Text
                    text_title =   "صندوق پس اندا ز واقف  (تاسيس 1359)  "  + "   تاريخ صدور: " + str(self.year) + "/" + str(self.month) 
                    # Reshape and Reorder the Text And Obtain It's Size
                    reshaped_text = arabic_reshaper.reshape(text_title)
                    display_text_title = get_display(reshaped_text)
                    text_title_size = draw.textsize(display_text_title, font=font_title)

                    # Set The Member Data Text
                    text_member = ("اطلاعات عضو" + "\n\n" +
                                   str(self.list["شماره عضويت"][bill_index]) + "    :  شماره عضويت" + "\n\n" +
                                   str(self.list["نام"][bill_index]) + " " +
                                   str(self.list["نام خانوادگي"][bill_index]) + "  :  نام عضو" + "\n\n" +
                                   f'{self.list["مبلغ پس انداز"][bill_index]:,}' + "  :  جمع پس انداز" + "\n\n" +
                                   f'{self.list["پس انداز ماهيانه"][bill_index]:,}' + "  :  پس انداز اين ماه" + "\n\n" +
                                   str(self.list["سرعت بازپرداخت"][bill_index]) + "  :  سرعت بازپرداخت" + "\n\n" +
                                   str(self.list["وضعيت قرعه کشي"][bill_index]) + "  :  وضعيت قرعه کشي" )
                    # Reshape and Reorder the Text And Obtain It's Size
                    reshaped_text = arabic_reshaper.reshape(text_member)
                    display_text_member = get_display(reshaped_text)                   


                    # Set The Loan Data Text
                    text_loan = ("اطلاعات وام" + "\n\n" +
                                   str(self.list["شماره وام"][bill_index]) + "    :  شماره وام" + "\n\n" +
                                   str(self.list["تاريخ (سال)"][bill_index]) + "/" +
                                   str(self.list["تاريخ (ماه)"][bill_index]) + "  :  تاريخ" + "\n\n" +
                                   f'{self.list["مبلغ وام"][bill_index]:,}' + "  :  مبلغ وام" + "\n\n" +
                                   f'{self.list["مبلغ اقساط"][bill_index]:,}' + "  :  مبلغ اقساط" + "\n\n" +
                                   f'{self.list["مانده بدهي"][bill_index]:,}' + "  :  مانده بدهي" + "\n\n" +
                                   str(self.list["اقساط باقي مانده"][bill_index]) + "  :  اقساط باقي مانده" )
                    # Reshape and Reorder the Text And Obtain It's Size
                    reshaped_text = arabic_reshaper.reshape(text_loan)
                    display_text_loan = get_display(reshaped_text)

                    # Set The Total Payment Text
                    text_total =   " جمع پرداختي  :      "  + f'{self.list["جمع پرداختي"][bill_index]:,}' + " تومان "
                    # Reshape and Reorder the Text And Obtain It's Size
                    reshaped_text = arabic_reshaper.reshape(text_total)
                    display_text_total = get_display(reshaped_text)
                    text_total_size = draw.textsize(display_text_total, font=font_title)

                    # Set The Signature Text
                    text_sign =   "امضاي حسابدار                                                     امضاي صندوق دار"
                    # Reshape and Reorder the Text And Obtain It's Size
                    reshaped_text = arabic_reshaper.reshape(text_sign)
                    display_text_sign = get_display(reshaped_text)
                    text_sign_size = draw.textsize(display_text_sign, font=font_content)
                    
                    # Draw the Rectangle
                    #draw.rectangle([(300, 300), (1000, 1000)], fill=None, outline ="green", width = 10)
                    # Draw the Circle
                    #draw.arc([(1000, 200), (1400, 600)], start = 0, end = 360, fill ="red", width = 10)
                    # Draw the text
                    #draw.text((x, y), display_text, fill='black', font=font)
                    
                    if (paragraph_index % 2 == 0):
                        # Calculate the position to draw the text
                        x_title = (horizontal_center - text_title_size[0]) // 2
                        x_member = left_margin
                        x_loan = left_margin + horizontal_center // 2
                        x_total = (horizontal_center - text_total_size[0]) // 2
                        x_sign = (horizontal_center - text_sign_size[0]) // 2
                        #Draw the line
                        draw.line([(0, (paragraph_index//2 + 1) * vertical_ofset),
                                   (img.width, (paragraph_index//2 + 1) * vertical_ofset)],
                                  fill ="Black", width = 5)
                        
                    else:
                        # Calculate the position to draw the text
                        x_title = (horizontal_center - text_title_size[0]) // 2 + horizontal_ofset
                        x_member = left_margin + horizontal_ofset
                        x_loan = left_margin + horizontal_center // 2 + horizontal_ofset
                        x_total = (horizontal_center - text_total_size[0]) // 2 + horizontal_ofset
                        x_sign = (horizontal_center - text_sign_size[0]) // 2 + horizontal_ofset

                    y_title = (top_margin + (paragraph_index//2) * vertical_ofset) - text_title_size[1]
                    y_member = (top_margin  + 30 + (paragraph_index//2) * vertical_ofset)
                    y_loan = (top_margin  + 30 + (paragraph_index//2) * vertical_ofset)
                    y_total = (top_margin + 520 + (paragraph_index//2) * vertical_ofset) - text_total_size[1]
                    y_sign = (top_margin + 590 + (paragraph_index//2) * vertical_ofset) - text_sign_size[1]
                    # Draw the text
                    draw.text((x_title, y_title), display_text_title, fill=(0, 0, 102, 255), font=font_title)
                    draw.text((x_member, y_member), display_text_member, fill='black', font=font_content)
                    draw.text((x_loan, y_loan), display_text_loan, fill='black', font=font_content)
                    draw.text((x_total, y_total), display_text_total, fill='black', font=font_title)
                    draw.text((x_sign, y_sign), display_text_sign, fill='black', font=font_content)
                    
                    # There Are 4 Paragraphs On Page (Page Is Divided By 4 Paragraphs Vertically)
                    paragraph_index += 1   

                    if((bill_index%bills_on_page == (bills_on_page - 1)) or (bill_index == bill_count - 1)):
                        
                        # Show the image
                        #img.show()
                        # Save the image
                        try:
                            os.mkdir('Payment')
                            filepath = ('Payment\Payment_' +
                                        str(self.year) + '_' +
                                        str(self.month) + '_' +
                                        str(paper_index) + '.png')
                            img.save(filepath)
                            paper_index += 1
                            paragraph_index = 0
                        except FileExistsError:
                            filepath = ('Payment\Payment_' +
                                        str(self.year) + '_' +
                                        str(self.month) + '_' +
                                        str(paper_index) + '.png')
                            img.save(filepath)
                            paper_index += 1
                            paragraph_index = 0

                return 1
            else:
                return 0
        except AttributeError:
            return 2
        
