## Current questions to be solved

1. Should we reduce boilerplate code for each client like `ApiClient`, `Config`, etc.
   1. Keep as is - Nothing to do, looks pretty ugly trying to use different clients in same project.
   2. Change `templates` in the client generator - difficult to implement for all clients since it is different
      specifications.
   3. Use `post_hooks` in generator to move all common code to a common library and update all imports - not as
      difficult as 2, but still need to maintain.
   4. Merge all specification into one and generate one library for everything. 
2. Auth options:
   1. Keep as is - nothing to do, not really comfortable to use our clients.
   2. Inheritance or template changing `ApiClient` to handle auth and refresh token logic.
   3. Using `Configuration.refresh_api_key_hook` - won't help for retry logic, since retry logic is in
3. Methods naming:
   1. Naming depends on `operationId` which has prefix in their names like (DataModel_AnalyticObjects,
       DataModel_Dimensions, DataModel_...). Renaming operationId to GetAnalyticObjects will help to make it clear.
   2. Changing templates to remove prefix from operationId.
4. Tests (copilot/gpt will make it faster, but still need to be done manually)
   1. Unit tests for DTOs - not quite sure that they are necessary.
   2. Integration tests - need to be implemented.