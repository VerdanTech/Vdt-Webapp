<script lang="ts">
	import { Verdagraph } from '@vdg-webapp/ui';

	import { workspace } from '$lib/seeds/workspace';
</script>

<Verdagraph contextParams={{ defaultSelectedWorkspaceId: workspace.id }} />
