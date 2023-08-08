class cumle_sonu:
    def __init__(self):
        self.soru = []
        self.unlem = []
        self.nokta = []
        self.virgul = []

    def classify_sentence(self, sentence):
        if sentence.endswith("?"):
            self.soru.append()
        elif sentence.endswith("!"):
            self.unlem.append()
        elif sentence.endswith("."):
            self.nokta.append()
        elif sentence.endswith(","):
            self.virgul.append()
        else:
            pass

if __name__ == "__main__":
    classifier = cumle_sonu('degisken')

    
