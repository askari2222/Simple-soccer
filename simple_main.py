cat > main.py << 'EOF'
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class DrawCheckerApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Title
        title = Label(
            text='🏟️ Draw Pattern Checker',
            font_size='20sp',
            size_hint_y=0.08,
            bold=True
        )
        main_layout.add_widget(title)
        
        # Refresh button
        refresh_btn = Button(
            text='Refresh Data',
            size_hint_y=0.08
        )
        refresh_btn.bind(on_press=self.refresh)
        main_layout.add_widget(refresh_btn)
        
        # Info section
        info = Label(
            text='Welcome to Draw Pattern Checker!\n\nThis app analyzes football matches for draw patterns.\n\nTap Refresh to load today\'s matches.',
            font_size='14sp',
            size_hint_y=0.84,
            text_size=(400, None)
        )
        main_layout.add_widget(info)
        
        return main_layout
    
    def refresh(self, instance):
        print("Refresh button pressed!")

if __name__ == '__main__':
    DrawCheckerApp().run()
EOF
