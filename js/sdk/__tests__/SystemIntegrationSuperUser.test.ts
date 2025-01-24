import { fuseClient } from "../src/index";
import { describe, test, beforeAll, expect } from "@jest/globals";

const baseUrl = "http://localhost:7272";

describe("fuseClient V3 Collections Integration Tests", () => {
  let client: fuseClient;

  beforeAll(async () => {
    client = new fuseClient(baseUrl);
    await client.users.login({
      email: "admin@example.com",
      password: "change_me_immediately",
    });
  });

  test("Get the health of the system", async () => {
    const response = await client.system.health();
    expect(response.results).toBeDefined();
  });

  test("Get the settings of the system", async () => {
    const response = await client.system.settings();
    expect(response.results).toBeDefined();
  });

  test("Get the status of the system", async () => {
    const response = await client.system.status();
    expect(response.results).toBeDefined();
  });
});
