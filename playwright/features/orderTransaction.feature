Feature: Order Transaction
  As a registered user
  I want to view my order details
  So that I can verify my order was placed successfully

  Scenario Outline: Verify order success message on order details page
    Given the user places an order using <username> and <password>
    And the user is on the landing page
    When the user logs into the portal using <username> and <password>
    And the user navigates to the orders page
    And the user selects the order ID
    Then the order success message should be displayed

    Examples:
      | username              | password   |
      | anshika@gmail.com     | Iamking@000 |