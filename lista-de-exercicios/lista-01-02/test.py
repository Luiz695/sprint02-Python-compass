import unittest

def my_map(list,f):
    nova_lista=[]
    
    for elemento in list:
        resultado = f()
        nova_lista.append(resultado)
    #print(nova_lista) 
    return nova_lista  
    
def default():
    return 2

'''-------------------------------------------''' 

class Testa_funcao_my_map(unittest.TestCase):
    def test(self):
        self.assertEqual(my_map([1, 2, 3, 4], default), [2, 2, 2, 2])
        #self.assertEqual(my_map([1, 2, 3, 4], default), [2, 2, 2, 2])
        
if __name__ == '__main__':
    unittest.main()