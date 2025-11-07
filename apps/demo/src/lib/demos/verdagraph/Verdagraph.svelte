<script lang="ts">
	import { Verdagraph } from '@vdg-webapp/ui';

	import { workspaceId } from './seed';
</script>

<Verdagraph contextParams={{ defaultSelectedWorkspaceId: workspaceId }} />
