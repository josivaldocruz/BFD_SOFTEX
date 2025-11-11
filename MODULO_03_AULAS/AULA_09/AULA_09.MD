REFACTORING site de padrões de projetos

https://refactoring.guru/refactoring

// A classe criadora declara o método fábrica que deve retornar
// um objeto de uma classe produto. As subclasses da criadora
// geralmente fornecem a implementação desse método. https://refactoring.guru/pt-br/design-patterns/factory-method
class Dialog is
    // A criadora também pode fornecer alguma implementação
    // padrão do Factory Method.
    abstract method createButton():Button

    // Observe que, apesar do seu nome, a principal
    // responsabilidade da criadora não é criar produtos. Ela
    // geralmente contém alguma lógica de negócio central que
    // depende dos objetos produto retornados pelo método
    // fábrica. As subclasses pode mudar indiretamente essa
    // lógica de negócio ao sobrescreverem o método fábrica e
    // retornarem um tipo diferente de produto dele.
    method render() is
        // Chame o método fábrica para criar um objeto produto.
        Button okButton = createButton()
        // Agora use o produto.
        okButton.onClick(closeDialog)
        okButton.render()


// Criadores concretos sobrescrevem o método fábrica para mudar
// o tipo de produto resultante.
class WindowsDialog extends Dialog is
    method createButton():Button is
        return new WindowsButton()

class WebDialog extends Dialog is
    method createButton():Button is
        return new HTMLButton()


// A interface do produto declara as operações que todos os
// produtos concretos devem implementar.
interface Button is
    method render()
    method onClick(f)

// Produtos concretos fornecem várias implementações da
// interface do produto.
class WindowsButton implements Button is
    method render(a, b) is
        // Renderiza um botão no estilo Windows.
    method onClick(f) is
        // Vincula um evento de clique do SO nativo.

class HTMLButton implements Button is
    method render(a, b) is
        // Retorna uma representação HTML de um botão.
    method onClick(f) is
        // Vincula um evento de clique no navegador web.


class Application is
    field dialog: Dialog

    // A aplicação seleciona um tipo de criador dependendo da
    // configuração atual ou definições de ambiente.
    method initialize() is
        config = readApplicationConfigFile()

        if (config.OS == "Windows") then
            dialog = new WindowsDialog()
        else if (config.OS == "Web") then
            dialog = new WebDialog()
        else
            throw new Exception("Error! Unknown operating system.")

    // O código cliente trabalha com uma instância de um criador
    // concreto, ainda que com sua interface base. Desde que o
    // cliente continue trabalhando com a criadora através da
    // interface base, você pode passar qualquer subclasse da
    // criadora.
    method main() is
        this.initialize()
        dialog.render()


