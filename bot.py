from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


class Bot(DesktopBot):
    def action(self, execution=None):
        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        #Opens the BotCity website.
        #self.execute(r'C:\Users\Platini\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Microsoft Teams.lnk')
        
        #if not self.find( "pesquisar", matching=0.97, waiting_time=30000):
        #    self.not_found("pesquisar")
        #self.click()
        #self.paste("leandro david metzker")
                
        #if not self.find( "leandro_david", matching=0.97, waiting_time=30000):
        #   self.not_found("leandro_david")
        #self.click()
                
        #if not self.find( "mensagem", matching=0.97, waiting_time=30000):
        #    self.not_found("mensagem")
        #self.click()
        
        #self.paste("Teste Python")

        #self.enter()

        
        # Bot_2

        self.browse("https://www.hashtagtreinamentos.com")    
        
        if not self.find( "curso_python", matching=0.97, waiting_time=20000):
            self.not_found("curso_python")
        self.click()

        if not self.find( "curso_carregou", matching=0.97, waiting_time=10000):
            self.not_found("curso_carregou")

        self.scroll_down(3000)

        if not self.find( "name", matching=0.97, waiting_time=10000):
            self.not_found("name")
        self.click()
        self.paste("Platini")
        
        if not self.find( "email", matching=0.97, waiting_time=10000):
            self.not_found("email")
        self.click()
        self.paste("platinigdr@hotmail.com")

        if not self.find( "cadastro", matching=0.97, waiting_time=10000):
            self.not_found("cadastro")
        self.click()
            

        # Uncomment to mark this task as finished on BotMaestro
        # self.maestro.finish_task(
        # task_id=execution.task_id,
        # status=AutomationTaskFinishStatus.SUCCESS,
        # message="Task Finished OK."
        # )

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()


























































































































