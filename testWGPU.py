from flask import Flask
import wgpu
import wgpu.backends.rs # import the backend module

app = Flask(__name__)

@app.route('/')
def hello_world():
    canvas = '<canvas id="myCanvas"></canvas>'

    # create a WebGPU device with the canvas element
    adapter = wgpu.request_adapter(canvas=None)
    device = adapter.request_device()

    # print information about the device
    device_info = {
        'name': device.name,
        'vendor': device.vendor_name,
        'backend': device.backend_name,
        'is_unified_memory': device.is_unified_memory,
        'limits': {
            'max_bind_groups': device.limits.max_bind_groups,
            'max_dynamic_uniform_buffers_per_pipeline_layout': device.limits.max_dynamic_uniform_buffers_per_pipeline_layout,
            'max_dynamic_storage_buffers_per_pipeline_layout': device.limits.max_dynamic_storage_buffers_per_pipeline_layout,
            'max_sampled_textures_per_shader_stage': device.limits.max_sampled_textures_per_shader_stage,
            'max_storage_buffers_per_shader_stage': device.limits.max_storage_buffers_per_shader_stage,
            'max_storage_textures_per_shader_stage': device.limits.max_storage_textures_per_shader_stage,
            'max_uniform_buffers_per_shader_stage': device.limits.max_uniform_buffers_per_shader_stage,
            'max_uniform_buffer_binding_size': device.limits.max_uniform_buffer_binding_size,
        }
    }
    print(device_info)

    return 'Hello, World!'

if __name__ == '__main__':
    app.run(port=5000, debug=True)
