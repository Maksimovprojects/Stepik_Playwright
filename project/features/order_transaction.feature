Feature: Order transaction

  Scenario Outline: Verify order details message shown in details page
    Given place the item order with <username> and <password>
    And the user is on landing page
    When I login to portal with <username> and <password>
    And navigate to orders page
    And select order id
    Then order message is successfully shown in details page
    Examples:
        |    username    | password  |
        | test@test.ru   | Resiver28  |