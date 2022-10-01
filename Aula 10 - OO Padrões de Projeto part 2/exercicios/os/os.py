import os


#Listar Comandos
#Memento
class Memento(object):
   def __init__(self,data):
      self.data = data

#Comandos
class Originator(object):
    def __init__(self,data):
       self.data = data

    def addComando(self,tipo):
        self.data = tipo

    def save(self):
        return Memento(self.data)

    def undo(self,memento):
       self.data = memento.data

#Caretaker
class ListaComandos(object):
    def __init__(self):
        self.mementos = list()
        self.originator = Originator("")

    def save(self):
        self.mementos.append(self.originator.save())

    def undo(self):
        if not len(self.mementos):
            return
        memento = self.mementos.pop()
        try:
            self.originator.undo(memento)
        except Exception:
            self.undo()

    def addComando(self,tipo):
        self.originator.addComando(tipo)
        self.save()

    def listar(self):
        #abrindo o arquivo
        file = open("log/cmds.txt", "r")
        print(file.read())
        file.close()

        #salvando entradas não listadas
        print("\nEntradas não listadas...")
        file = open("log/cmds.txt", "a")
        for x in self.mementos:
            print(x.data)
            file.write(f'{x.data}\n')
        file.close()
        self.mementos = []



import math

#Ativar
#Subject
class Ativador(object):
   def __init__(self):
       pass

   def ativar(self):
       file = open('mat/mat.mat')
       mat = file.read()
       mat = map(int,mat.replace('\n','').split(','))

       aux = []
       for x in mat:
           aux.append([x, (1/(1+ math.exp(-x)))])
       return aux

class RealSubject(Ativador):
    def __init__(self):
        pass

class ProxySubject(Ativador):
    def __init__(self,*args,**kwargs):
        self.real = None
        self.cache = None

    def ativar(self):
        if self.real is None:
            self.real = RealSubject()

        self.pre_operation()
        if self.cache is None:
            self.cache = self.real.ativar()
        self.post_operation()
       # self.printCache(self.cache)
        return self.cache

    def pre_operation(self):
        pass

    def post_operation(self):
        pass

    def printCache(self,data):
       for i in data:
          print(i)



#interator

#Arquivo
class Iterable(object):
   def __init__(self,path,size):
      self.path = path
      self.size = size

#Pasta
class Container(object):
   def __init__(self):
      self.data = list()

   def __iter__(self):
      return Iterator(self)

   def addItem(self,item):
      self.data.append(item)
   
   def get_ith(self,i):
      if len(self.data) > i:
         return self.data[i]
      return None

class Iterator(object):
   def __init__(self,container):
      self.container = container
      self.current = 0

   def __next__(self):
      value = self.container.get_ith(self.current)
      if value is None:
         #raise StopIteration
         return value
      self.current+=1
      return value



#visualizar
class Arquivos(object):
   def __init__(self):
       self.folders = list()
       
   def convert_size(self,size_bytes):
      if size_bytes == 0:
         return "0B"
      size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
      i = int(math.floor(math.log(size_bytes, 1024)))
      p = math.pow(1024, i)
      s = round(size_bytes / p, 2)
      return "%s %s" % (s, size_name[i])

   def fillContainer(self):
      list_dir = ['mat','log','files','files/imgs','files/others']
      
      
      for dir_path in list_dir:
         
         dir = os.listdir(dir_path)
         #create container
         c = Container()
         for x in dir:
                     
            if os.path.isfile(dir_path + "/" + str(x)):
               
               path = dir_path + "/" + str(x)
               size = os.path.getsize(dir_path + "/" + str(x))
               i = Iterable(path,size)
               
               c.addItem(i)
               
         self.folders.append(c)
      

    
   def ListFiles(self):
      self.fillContainer()
      for i in self.folders:
         j = i.__iter__()
         total_folder_size = 0
         
         while(1):
            intera = j.__next__()
            if intera is None:
               break
            print(intera.path)
            size = intera.size
            total_folder_size += size
            print(self.convert_size(int(size)))

         print("tamanho total da pasta " + self.convert_size(total_folder_size))
        
   

   







def main():
    l = ListaComandos()
    a = ProxySubject()
    arq = Arquivos()
    while(1):
        print("1 - Listar histórico de comandos executados")
        print("2 - Operação de Ativação (Calculo Função Sigmoide Logística)")
        print("3 - Contabilizar arquivos e tamanhos em suas pastas")

        opcao = str(input('Escolha uma opção: '))

        if opcao == "1":
            l.addComando("listar")
            l.listar()

        if opcao == "2":
            l.addComando("ativar")
            a.ativar()

        if opcao == "3":
            l.addComando("visualizar")
            arq.ListFiles()
            

if __name__ == "__main__":
    main()
