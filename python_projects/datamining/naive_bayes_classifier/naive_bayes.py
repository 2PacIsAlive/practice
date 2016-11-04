#usr/bin/env python

from pandas      import read_csv
from collections import Counter

class NaiveBayesClassifier:
    
    def __init__(self):
        self.data = read_csv('NaiveBayesLoanDecision.csv', header=0)
        self.frequencies         = {column: Counter(self.data[column]) for column in self.data}
        self.label_probabilities = {value:  self.frequencies['Loan Decision'][value] / float(len(self.data['Loan Decision'])) for value in self.frequencies['Loan Decision'].keys()} 

    def predict(self, entry):
        probabilities = {attribute: {classification: None for classification in self.label_probabilities.keys()} for attribute in self.frequencies if attribute != 'Loan Decision'}
        for attribute in probabilities:
            for classification in probabilities[attribute]:
                probabilities[attribute][classification] = len([x for x in self.frequencies[attribute] 

def main():
    classifier = NaiveBayesClassifier()
    classifier.predict({'Home Owner':     'Yes', 
                        'Marital Status': 'Married', 
                        'Annual Income':  '75K'})

if __name__=='__main__': main()
