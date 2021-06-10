describe("Order a meal", () => {
  it("Successfully order a large vegetarian pizza", () => {
    cy.visit("/order-meal/");
    cy.get("[data-cy-meal]")
      .select("Large Vegetarian Pizza (serves 3)")
      .blurAndWaitForHTMX();
    cy.get("[data-cy-num-people]").clear();
    cy.get("[data-cy-num-people]").type("6").blurAndWaitForHTMX();
    cy.get("[data-cy-vegetarian]").click().blurAndWaitForHTMX();
    cy.get("[data-cy-order-button]").click();
    cy.contains("Order successfully placed!");
  });
});
