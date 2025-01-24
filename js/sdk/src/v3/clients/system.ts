import { feature } from "../../feature";
import { fuseClient } from "../../fuseClient";
import {
  WrappedGenericMessageResponse,
  WrappedServerStatsResponse,
  WrappedSettingsResponse,
} from "../../types";

export class SystemClient {
  constructor(private client: fuseClient) {}

  /**
   * Check the health of the FUSE server.
   */
  @feature("system.health")
  async health(): Promise<WrappedGenericMessageResponse> {
    return await this.client.makeRequest("GET", "health");
  }

  /**
   * Get the configuration settings for the FUSE server.
   * @returns
   */
  @feature("system.settings")
  async settings(): Promise<WrappedSettingsResponse> {
    return await this.client.makeRequest("GET", "system/settings");
  }

  /**
   * Get statistics about the server, including the start time, uptime,
   * CPU usage, and memory usage.
   * @returns
   */
  @feature("system.status")
  async status(): Promise<WrappedServerStatsResponse> {
    return await this.client.makeRequest("GET", "system/status");
  }
}
