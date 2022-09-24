from entidadesDados import pessoas, trabalho
from discoUtils import util

if __name__ == '__main__':

    p = trabalho.Projeto(4523,1000000)
    print(p)

    car = trabalho.Cargo(3,"programador",4344)
    print(car)

    e = pessoas.Empregado(7,"renan",car.nome,p.id)
    print(e)
    
    cli = pessoas.Cliente(1,"dril",p.id)
    print(cli)
    
    w = util.Write()
    r = util.Reader()

    
    w.write(p)
    w.write(car)
    w.write(e)
    w.write(cli)
    
    r.read("Cliente_23.json")
    r.read("Cargo_3.json")
    r.read("Empregado_7.json")
    r.read("Projeto_4523.json")
