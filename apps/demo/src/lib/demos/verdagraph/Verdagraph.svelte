<script lang="ts">
	import { getContext } from 'svelte';

	import { CONTROLLER_CONTEXT_ID, type ControllerContext } from '@vdg-webapp/models';
	import { Verdagraph, setGardenContext } from '@vdg-webapp/ui';

	import { gardenId, workspaceId } from './seed';

	const controller = getContext<ControllerContext>(CONTROLLER_CONTEXT_ID);
	const garden = setGardenContext(controller);
	garden.id = gardenId;
</script>

<Verdagraph
	gardenId={garden.id}
	contextParams={{ defaultSelectedWorkspaceId: workspaceId }}
/>
