from .tleng2 import RendererMethods

def import_params_needed() -> None:
    RendererMethods.import_scene_renderer_params_list({
        'free_roam':{
            'display' : RendererMethods.load_local_display_ratio(1/2),
            'camera' : None
        } 
    })