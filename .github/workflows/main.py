import flet as ft
import asyncio


win_color = 'orange'
cursor_colorrr = 'black'
focus_fild_border = 'green'
unfocus_fild_border = 'black'
unfocus_txt_color = 'black'
focus_txt_color = 'red'
paddingg = ft.padding.all(5)
txt_capitall = None
hint_txt_color = 'black'
unfocus_txt_label_color = 'blue'
#
#
# unfocus_drp_text_color = 'black'
# unfocus_drp_border_color = 'black'
# focus_drp_text_color = 'red'
# focus_drp_bg_color = 'pink'
# def Custome_Textfield(label_name,Hint_name):
#     custom_field = ft.TextField(label=label_name,hint_text=Hint_name,text_align=ft.TextAlign.CENTER,
#                              cursor_color = cursor_colorrr,
#                              focused_border_color=focus_fild_border,
#                              border_color=unfocus_fild_border,
#                             color=unfocus_txt_color,
#                             focused_color=focus_txt_color,
#                             content_padding=paddingg,
#                             capitalization=txt_capitall,
#                             hint_style=ft.TextStyle(color=hint_txt_color),
#                             label_style=ft.TextStyle(color=unfocus_txt_label_color,size=20))
#     return custom_field
# def registrationnn(page):
#     # page.window.width = 400
#     # page.window_height = 600
#
#     page.title='Johnny Registration'
#     page.bgcolor=win_color
#
#     topTitle = 'Registration'
#     page.theme_mode = 'light'
#
#
#     d = ft.Dropdown(hint_text='select',
#                  color=unfocus_drp_text_color,
#                  options=[ft.dropdown.Option('Customer'),
#                           ft.dropdown.Option('Sunar'),
#                           ],
#                  border_radius=30,
#                  hint_style=ft.TextStyle(color=unfocus_drp_text_color, size=20),
#
#                  alignment=ft.alignment.center, filled=True,
#                  bgcolor=win_color,
#                  border_color=unfocus_drp_border_color,
#                  focused_color=focus_drp_text_color,
#                  focused_bgcolor=focus_drp_bg_color,
#                  text_style=ft.TextStyle(color=ft.colors.WHITE,size=20)
#                  )
#
#     top_title = ft.Row(controls=[ft.Text(value=topTitle,size=20,color='White',italic=True,text_align=ft.alignment.center,)],
#                     alignment=ft.MainAxisAlignment.CENTER)
#
#     Customer_type = ft.Row(controls=[d],alignment=ft.MainAxisAlignment.CENTER)
#     c_name = Custome_Textfield(label_name='Name', Hint_name='enter name')
#     nik_name = Custome_Textfield(label_name='Nick name', Hint_name='enter nick name')
#     find_name = Custome_Textfield(label_name='Find name', Hint_name='enter find name')
#
#     OTP1_btn = ft.ElevatedButton(text='OTP',width=80)
#     OTP2_btn = ft.ElevatedButton(text='OTP',width=80)
#
#     mob1 = Custome_Textfield(label_name='Mobile no.1', Hint_name='enter mobile number')
#     mob2 = Custome_Textfield(label_name='Mobile no.2', Hint_name='enter mobile number')
#
#     mob1.width = page.window.width * 0.6
#     mob2.width = page.window.width * 0.6
#
#     cc = ft.Column(controls=[ft.Row(controls=[mob1,OTP1_btn]),ft.Row(controls=[mob2,OTP2_btn])],expand=True)
#
#     father_nm = Custome_Textfield(label_name="Father's", Hint_name='enter father')
#     mother_nm = Custome_Textfield(label_name="Mother's", Hint_name='enter mother')
#     husband_nm = Custome_Textfield(label_name="Husband's", Hint_name='enter husband')
#     wife_nm = Custome_Textfield(label_name="Wife's", Hint_name='enter wife')
#     child_nm = Custome_Textfield(label_name="Children's", Hint_name='enter child')
#
#     address = Custome_Textfield(label_name='Address', Hint_name='enter address....')
#     village = Custome_Textfield(label_name='Village', Hint_name='enter village')
#     city = Custome_Textfield(label_name='City', Hint_name='enter city')
#     state = Custome_Textfield(label_name='State', Hint_name='enter state')
#     country = Custome_Textfield(label_name='Country', Hint_name='enter country')
#
#     comment_box = Custome_Textfield(label_name='Comment BOX', Hint_name='type.....')
#
#
#
#     Submit_btn = ft.ElevatedButton(text='Submit',width=page.window.width*0.5,bgcolor=ft.colors.RED,color='yellow')
#     Search_btn = ft.ElevatedButton(text='Search',width=page.window.width*0.3)
#     Update_btn = ft.ElevatedButton(text='Update',width=page.window.width*0.3,bgcolor='blue',color='white')
#     Clear_btn = ft.ElevatedButton(text='Empty',width=page.window.width*0.3,bgcolor='black',color='white')
#     Next_btn = ft.ElevatedButton(text='Next',width=page.window.width,bgcolor=ft.colors.YELLOW,color=ft.colors.BLACK)
#
#     update_id = ft.TextField(label='search id',width=page.window.width*0.25,color='white',label_style=ft.TextStyle(color='white'))
#     btn_group = ft.Column(controls=[ft.Row(controls=[Search_btn,update_id,Update_btn])],horizontal_alignment=ft.CrossAxisAlignment.CENTER)
#
#
#     conttainerr = ft.ListView(controls=[Customer_type,c_name,nik_name,find_name,
#                                      ft.Container(height=15),
#                                      cc,
#                                      ft.Container(height=15),
#                                                      father_nm,mother_nm,husband_nm,wife_nm,child_nm,
#                                         ft.Container(height=15),
#                                      address,village,city,state,country,comment_box,ft.Row(controls=[Submit_btn,Clear_btn]),
#                                      ft.Container(height=30),
#                                      btn_group, ft.Container(height=30),
#                                      Next_btn, ft.Container(height=10)
#                                      ],
#                            expand=True,spacing=10)
#
#     # bhbh = page.add(top_title,
#     #          Container(content=conttainerr,width=page.window.width*0.9,margin=margin.only(0,10,0,0)),
#     #          )
#
#     bhbh = ft.Column(controls=[top_title,
#                     ft.Container(content=conttainerr, width=page.window.width * 0.9, margin=ft.margin.only(0, 10, 0, 0))],
#                     scroll=ft.ScrollMode.AUTO,alignment=ft.alignment.center)
#     # page.scroll="always"
#     #
#     # page.horizontal_alignment='center'
#     # page.update()
#     return bhbh
#
# def run_my_app(page:ft.page):
#     page.add(registrationnn(page))
#     page.scroll = True
#     page.update()
#
# if __name__ == "__main__":
#     ft.app(target=run_my_app)

# flet main.py
# cd F:\software_file_downloaded\python_practice\Flet\android_vali_flet

def Custome_Textfield(label_name,Hint_name):
    custom_field = ft.TextField(label=label_name,hint_text=Hint_name,text_align=ft.TextAlign.LEFT,
                             cursor_color = 'black',
                             focused_border_color='green',
                             border_color='black',
                            color='black',
                            focused_color='black',bgcolor='white',
                            content_padding=paddingg,
                            capitalization=txt_capitall,
                            hint_style=ft.TextStyle(color='#757575'),
                            label_style=ft.TextStyle(color='black',size=17,weight=ft.FontWeight.W_600))
    return custom_field
class android_login_uidesign(ft.Column):
    def __init__(self,page:ft.Page,application_name:str="Jewellery Software",
                 title_name:str="JOHNNY Software's",title_color:str="#770E0E",title_size:int=20,title_style="bold",
                 page_bg_color:str="#FFFCE2",center_box_bg_color:str="#FFEBA2",login_btn_text:str="Login",
                 login_btn_txt_color:str="white",login_btn_bg_color:str="black",
                 message_text_color:str="#E12020",*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.application_name = application_name
        self.title_name = title_name
        self.title_color = title_color
        self.title_size = title_size
        self.title_style = title_style
        self.page_bg_color = page_bg_color
        self.center_box_bg_color = center_box_bg_color
        self.login_btn_text = login_btn_text
        self.login_btn_txt_color = login_btn_txt_color
        self.login_btn_bg_color = login_btn_bg_color
        self.message_text_color = message_text_color
        self.login_command = None

    def build(self):
        self.email_widgets = Custome_Textfield('Email','enter email id')
        self.passs_widgets = Custome_Textfield('Password', 'enter password')
        self.pinn_widgets = Custome_Textfield('PIN', 'enter PIN')
        self.msg_widgets = ft.Text('Message here',color=self.message_text_color,visible=False)

        self.title_widgets = ft.Text(self.title_name,size=self.title_size,color=self.title_color,font_family='Inter',weight=ft.FontWeight.BOLD)
        space_wd = ft.Text('')
        self.login_btn_widgets = ft.ElevatedButton(self.login_btn_text, color=self.login_btn_txt_color,
                                                   width=int(self.page.window.width * 0.3),
                                                   bgcolor=self.login_btn_bg_color, on_click=self.login_commandd,
                                                   style=ft.ButtonStyle(text_style=ft.TextStyle(size=20),
                                                                        padding=ft.padding.only(20, 10, 20, 15)))
        # bottom text column and widgets
        bottom_text1 = ft.Text("PAID", font_family='Inter', color='#29B909', weight=ft.FontWeight.BOLD,
                               spans=[ft.TextSpan(" Software's", ft.TextStyle(italic=True, color='#03051F',
                                                                              weight=ft.FontWeight.BOLD))])
        bottom_text2 = ft.Text('JOHNNY Developer', color='#7A1410', font_family='Inter', weight=ft.FontWeight.BOLD)
        bottom_column = ft.Column([bottom_text1, bottom_text2],
                                  alignment=ft.MainAxisAlignment.END,
                                  horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=1)



        self.card_inner_controls_list = [self.email_widgets,self.passs_widgets,self.pinn_widgets,self.msg_widgets]
        card_inner_column = ft.Column(controls=self.card_inner_controls_list,alignment=ft.alignment.center,spacing=10,wrap=False,
                                  horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        container_boxx = ft.Container(content=card_inner_column,padding=10)
        center_card = ft.Card(content=container_boxx,color=self.center_box_bg_color,expand=False,width=int(self.page.window.width-10))


        upper_column = ft.Column([self.title_widgets,center_card,self.login_btn_widgets],
                                 alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,expand=True)

        page_column_list = [upper_column,bottom_column]
        page_column = ft.Column(controls=page_column_list,height=int(self.page.window.height-50),
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        return page_column
    async def login_commandd(self,e):
        if self.email_widgets.value == "":
            await self.show_msg('please enter email id')
        elif len("".join(self.email_widgets.value.split()))<7:
            await self.show_msg('please enter correct emil id')
        elif self.passs_widgets.value == "":
            await self.show_msg('please enter password')
        elif len("".join(self.passs_widgets.value.split()))<8:
            await self.show_msg('password must have atleast 8 characters')
        elif (self.pinn_widgets.value == ""):
            await self.show_msg('please enter PIN')
        elif "".join(self.pinn_widgets.value.split()).isdigit() == False:
            await self.show_msg('enter only digits')
        elif len("".join(self.pinn_widgets.value.split()))<4:
            await self.show_msg('PIN must have atleast 4 characters')
        else:
            if self.login_command != None:
                self.login_command()

    def all_field_get_parameter(self):
        return {'application_name':"".join(self.application_name.split()),
                'software_title':self.title_name,
                'email':"".join(self.email_widgets.value.split()),
                'pwd':"".join(self.passs_widgets.value.split()),
                'pin':"".join(self.pinn_widgets.value.split())}
    def empty_all_field(self):
        self.email_widgets.value = ''
        self.passs_widgets.value = ''
        self.pinn_widgets.value = ''
        self.msg_widgets.value = ''
        self.update()
    async def show_msg(self,msg_string):
        self.msg_widgets.visible = True
        self.msg_widgets.value = str(msg_string)
        self.update()
        await asyncio.sleep(5)
        self.msg_widgets.value = ''
        self.msg_widgets.visible = False
        self.update()
    def set_email_field_value(self,email_txt:str):
        self.email_widgets.value = str("".join(email_txt.split()))
        self.update()



def main(page:ft.Page):
    # page.window.width = 360
    # page.window.height = 640
    page.bgcolor = '#FFFACA'
    page.adaptive = True
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    acc = android_login_uidesign(page)

    # def shhh():
    #     acc.show_msg('doneeee')
    # acc.login_command = shhh
    page.add(acc)
    page.update()

# if __name__ == "__main__":
ft.app(target=main)

# flet main.py
# cd F:\software_file_downloaded\python_practice\Flet\android_vali_flet
