Cypress.Commands.add("waitForHTMX", () => {
  cy.get(".htmx-request", {
    timeout: Cypress.config("pageLoadTimeout"),
  }).should("not.exist");
});

Cypress.Commands.add("blurAndWaitForHTMX", () => {
  cy.focused().blur().waitForHTMX();
});
