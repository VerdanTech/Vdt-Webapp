<script lang="ts">
    import { melt, createTreeView, type TreeView } from '@melt-ui/svelte';
    import type { WorkspaceFullSchema } from '$codegen';
    import activeWorkspace from '../activeWorkspace.svelte';

    type Props = {
        workspace: WorkspaceFullSchema
    }

    let {workspace}: Props = $props();

    const treeView = createTreeView();
</script>

<!-- Workspace name -->

<!-- Workspace description -->

<!-- Planting area trees -->

<!-- Planting area name -->

<!-- Planting area description -->

<!-- Planting area geometries -->

<!-- Geometry type -->

<!-- Geometry attributes -->

<!-- Rectangle attributes -->

<!-- Polygon attributes -->

<!-- Ellipse attributes -->

<!-- Lines attributes -->

<!-- Scale factor -->

<!-- Rotation -->

<!-- Nulled -->

<!-- Planting area locations -->

<!-- Planting area depth -->

<!-- Planting area movable -->
