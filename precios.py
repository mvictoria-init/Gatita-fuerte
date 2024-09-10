class Precios:
    def __init__(self, mensual=None, trimestral=None, anual=None):
        self.mensual = mensual
        self.trimestral = trimestral
        self.anual = anual
    
    def __str__(self):
        return (f'''Los precios son:
                Mensual: {self.mensual}
                Trimestral: {self.trimestral}
                Anual: {self.anual}
                ''')