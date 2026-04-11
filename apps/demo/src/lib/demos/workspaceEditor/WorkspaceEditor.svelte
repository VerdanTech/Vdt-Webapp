<script lang="ts">
	import { WorkspaceEditor } from '@vdg-webapp/ui';

	import { workspace } from '$lib/seeds';
</script>

<WorkspaceEditor defaultId={workspace.id} includeWorkspacesMenu={false} />
