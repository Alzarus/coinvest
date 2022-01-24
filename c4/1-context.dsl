workspace {

    model {
        user = person "Usuário"
        dashboard = softwareSystem "Dashboard" "Apresenta a interface que o usuário acessa para ler os gráficos"
        persistance = softwareSystem "Dados armazenados" "Armazena os dados coletados"
        collector = softwareSystem "Coletor de dados" "Coleta os dados externos sobre criptomoedas"
        
        

        user -> dashboard "Acessa e lê os dados"
        dashboard -> persistance "Busca os dados armazenados, trata e os apresenta no gráfico"
        collector -> persistance "Coleta os dados e os salva com segurança"
    }

    views {
        systemContext dashboard {
            include *
            autolayout
        }

        theme default
        
    }
    
}