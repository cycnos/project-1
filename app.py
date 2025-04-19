from kivy.config import Config
from kivy.lang import Builder
from kivymd.app import MDApp




KV = '''

MDScreen:
    

    MDNavigationLayout:

        MDScreenManager:
            Screen:
                name: "main_screen"





                Image : 
                    source : "Background1.png"
                    allow_stretch: True
                    keep_ratio: False
                    ripple_behavior: "False"
                    pos_hint: {"center_x": .5, "center_y": .5}

                

                MDTextField:
                    mode: "outlined"
                    size_hint_x: None
                    
                    width: "240dp"
                    height: 20
                    radius: [dp(10)]
                    pos_hint: {"center_x": .5, "center_y": .61}
                    theme_bg_color_normal: "#272727"
                    color_normal : "black"
                    color_focus :"black"

                    

                    

                    MDTextFieldLeadingIcon:
                        icon: "account"
                        theme_icon_color: "Custom"
                        icon_color_normal: "black"
                        icon_color_focus: "black"

                    MDTextFieldHintText:
                        text: "Username"
                        theme_icon_color: "Custom"
                        text_color_normal: "black"
                        text_color_focus: "black"
                        



                MDTextField:
                    mode: "outlined"
                    size_hint_x: None
                    password: True
                    width: "240dp"
                    height: 20
                    radius: [dp(10)]
                    pos_hint: {"center_x": .5, "center_y": .50}
                    color_normal: "grey"
                    
                    

                    MDTextFieldLeadingIcon:
                        icon: "lock"
                        theme_icon_color: "Custom"
                        icon_color_normal: "black"
                        icon_color_focus: "black"
                        

                    MDTextFieldHintText:
                        text: "Password"
                        text_color_normal: "black"
                        text_color_focus: "black"

                MDIconButton:
                    id : show_password_button
                    
                    icon: "eye-off-outline"
                    pos_hint: {"center_x": .75, "center_y": .50}
                    
                    theme_icon_color: "Custom"
                    icon_color : "black"
                    on_release: root.ids.show_password_button.icon = "eye-outline"


                MDButton:
                    style: "text"
                    pos_hint: {"center_x": .5, "center_y": .30}
                    on_release:
                        print("Mot de passe oublie")
                
                    ripple_behavior: False  # Désactive l'effet ripple
                    # Enlève l'effet de survol
                    hover_color: [0, 0, 0, 0]  # La couleur du survol devient complètement transparente
                    background_normal: ""  # Désactive les effets visuels de l'arrière-plan
                
                    MDButtonText:
                        text: "Forgot password?"
                        theme_text_color: "Custom"
                        text_color: "#000000"
                        font_size: dp(14)
                        bold: True
                        halign: "center"



                        
                               


                

                MDLabel:
                    text: "Don't have an account ?"
                    font_style : "Label"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: "#000000"  # Texte blanc pour contraste
                    pos_hint: {"center_x": 0.5, "center_y": 0.16}
                    


                MDButton:
                    style: "elevated"
                    theme_text_color: "Custom"
                    text_color: "#000000"
                    pos_hint: {"center_x": .5, "center_y": .1}
                    height: dp(50)
                    width: dp(100)
                    radius: [dp(25)]
                    MDButtonText:
                        width: dp(100)
                        style: "elevated"
                        theme_text_color: "Custom"
                        text_color: "black"
                        text: "Sign Up"
                        bold: True
                        font_size: dp(20)
                        valign: "center"
                        halign: "center"
                        size_hint: None, None



                    












                MDButton:
                    style: "elevated"
                    theme_text_color: "Custom"
                    text_color: "#000000"
                    pos_hint: {"center_x": .5, "center_y": .38}
                    height: dp(50)
                    width: dp(250)
                    radius: [dp(25)]


                    MDButtonText:
                        width: dp(250)
                        style: "elevated"
                        theme_text_color: "Custom"
                        text_color: "black"
                        text: "Log In"
                        bold: True
                        font_size: dp(20)
                        valign: "center"
                        halign: "center"
                        padding: dp(30)  # espace autour du texte
                        size_hint: None, None
                        spacing: dp(10)  # espace entre le texte et le bouton



                    
                    
            
                    

'''

class Example(MDApp):
    def build(self):

        self.theme_cls.theme_style_switch_animation = True
        
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

    
        



Example().run()
#18/04 ---