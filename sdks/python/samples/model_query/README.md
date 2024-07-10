## Current Questions to be Solved

1. Should we reduce boilerplate code for each client like `ApiClient`, `Config`, etc.?
   1. Keep as is - lots of duplicates when using different clients in the same project.
   2. Change `templates` in the client generator - difficult to implement for all clients since they have different specifications.
   3. Use `post_hooks` in the generator to move all common code to a common library and update all imports - not as difficult as option 2, but still needs maintenance.
   4. Merge all specifications into one and generate one library for everything.
For now, we will go with option 1 and leave everything as is.

2. Auth options:
   1. Keep as is - nothing to do, but not really comfortable to use.
   2. Change template for `ApiClient` to handle auth and refresh token logic.
   3. Change template for `Configuration` and use `refresh_api_key_hook` to handle auth and refresh token logic. 
update templates for 'ApiClient' and 'Configuration' to handle auth and refresh token logic.

3. Method naming:
   1. Naming depends on `operationId` which has a prefix in their names like (`DataModel_AnalyticObjects`, `DataModel_Dimensions`, `DataModel_...`).
Check if it is possible to update methods naming in the templates.

4. Tests (copilot/gpt will make it faster, but still need to be done manually)
   1. Unit tests for DTOs - not quite sure that they are necessary.
   2. Integration tests - need to be implemented.
