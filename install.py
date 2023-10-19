import launch

def install():
    print("Installing extension 'stable-diffusion-webui-tensorrt'")

    if not launch.is_installed("tensorrt"):
        raise ModuleNotFoundError("could not find tensorrt python module")

    if not launch.is_installed("pycuda"):
        launch.run_pip(f'install pycuda', "pycuda")

    if not launch.is_installed("onnx"):
        launch.run_pip(f'install onnx', "onnx")

    # Polygraphy	
    if not launch.is_installed("polygraphy"):
        print("Polygraphy is not installed! Installing...")
        launch.run_pip("install polygraphy --extra-index-url https://pypi.ngc.nvidia.com", "polygraphy", live=True)

    print("done installing extension 'stable-diffusion-webui-tensorrt'")
 
install()