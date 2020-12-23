# trace generated using paraview version 5.7.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Legacy VTK Reader'
combustor2Dwf_ = LegacyVTKReader(FileNames=['/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/VTK/combustor2D-wf_0.vtk', '/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/VTK/combustor2D-wf_454.vtk', '/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/VTK/combustor2D-wf_909.vtk', '/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/VTK/combustor2D-wf_1399.vtk', '/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/VTK/combustor2D-wf_2135.vtk', '/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/VTK/combustor2D-wf_2977.vtk', '/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/VTK/combustor2D-wf_3845.vtk', '/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/VTK/combustor2D-wf_4708.vtk', '/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/VTK/combustor2D-wf_5532.vtk', '/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/VTK/combustor2D-wf_6279.vtk', '/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/VTK/combustor2D-wf_6938.vtk'])

# get animation scene
animationScene1 = GetAnimationScene()

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1435, 795]

# show data in view
combustor2Dwf_Display = Show(combustor2Dwf_, renderView1)

# trace defaults for the display properties.
combustor2Dwf_Display.Representation = 'Surface'

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on animationScene1
animationScene1.AnimationTime = 2.0

# Properties modified on timeKeeper1
timeKeeper1.Time = 2.0

# set scalar coloring
ColorBy(combustor2Dwf_Display, ('POINTS', 'C7H16'))

# rescale color and/or opacity maps used to include current data range
combustor2Dwf_Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
combustor2Dwf_Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'C7H16'
c7H16LUT = GetColorTransferFunction('C7H16')
c7H16LUT.RGBPoints = [0.0, 0.0, 0.0, 0.34902, 0.0022703860886394978, 0.039216, 0.062745, 0.380392, 0.0045407721772789955, 0.062745, 0.117647, 0.411765, 0.006811158265918493, 0.090196, 0.184314, 0.45098, 0.009081544354557991, 0.12549, 0.262745, 0.501961, 0.011351930443197489, 0.160784, 0.337255, 0.541176, 0.013622316531836987, 0.2, 0.396078, 0.568627, 0.015892702620476484, 0.239216, 0.454902, 0.6, 0.018163088709115982, 0.286275, 0.521569, 0.65098, 0.02043347479775548, 0.337255, 0.592157, 0.701961, 0.022703860886394978, 0.388235, 0.654902, 0.74902, 0.024974246975034475, 0.466667, 0.737255, 0.819608, 0.027244633063673973, 0.572549, 0.819608, 0.878431, 0.02951501915231347, 0.654902, 0.866667, 0.909804, 0.03178540524095297, 0.752941, 0.917647, 0.941176, 0.034055791329592466, 0.823529, 0.956863, 0.968627, 0.036326177418231964, 0.988235, 0.960784, 0.901961, 0.036326177418231964, 0.941176, 0.984314, 0.988235, 0.03777922451496125, 0.988235, 0.945098, 0.85098, 0.039232271611690524, 0.980392, 0.898039, 0.784314, 0.04086694959551096, 0.968627, 0.835294, 0.698039, 0.04313733568415046, 0.94902, 0.733333, 0.588235, 0.045407721772789955, 0.929412, 0.65098, 0.509804, 0.04767810786142945, 0.909804, 0.564706, 0.435294, 0.04994849395006895, 0.878431, 0.458824, 0.352941, 0.05221888003870845, 0.839216, 0.388235, 0.286275, 0.054489266127347946, 0.760784, 0.294118, 0.211765, 0.056759652215987444, 0.701961, 0.211765, 0.168627, 0.05903003830462694, 0.65098, 0.156863, 0.129412, 0.06130042439326644, 0.6, 0.094118, 0.094118, 0.06357081048190594, 0.54902, 0.066667, 0.098039, 0.06584119657054543, 0.501961, 0.05098, 0.12549, 0.06811158265918493, 0.45098, 0.054902, 0.172549, 0.07038196874782443, 0.4, 0.054902, 0.192157, 0.07265235483646393, 0.34902, 0.070588, 0.211765]
c7H16LUT.ColorSpace = 'Lab'
c7H16LUT.NanColor = [0.25, 0.0, 0.0]
c7H16LUT.Discretize = 0
c7H16LUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'C7H16'
c7H16PWF = GetOpacityTransferFunction('C7H16')
c7H16PWF.Points = [0.0, 0.0, 0.5, 0.0, 0.07265235483646393, 1.0, 0.5, 0.0]
c7H16PWF.ScalarRangeInitialized = 1

# create a new 'OpenFOAMReader'
combustorfoam = OpenFOAMReader(FileName='/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/combustor.foam')

# show data in view
combustorfoamDisplay = Show(combustorfoam, renderView1)

# trace defaults for the display properties.
combustorfoamDisplay.Representation = 'Surface'

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(combustorfoamDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
combustorfoamDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')
vtkBlockColorsLUT.InterpretValuesAsCategories = 1
vtkBlockColorsLUT.AnnotationsInitialized = 1
vtkBlockColorsLUT.RGBPoints = [270962.9375, 0.0, 0.0, 0.34902, 287793.33984375, 0.039216, 0.062745, 0.380392, 304623.7421875, 0.062745, 0.117647, 0.411765, 321454.14453125, 0.090196, 0.184314, 0.45098, 338284.546875, 0.12549, 0.262745, 0.501961, 355114.94921875, 0.160784, 0.337255, 0.541176, 371945.3515625, 0.2, 0.396078, 0.568627, 388775.75390625, 0.239216, 0.454902, 0.6, 405606.15625, 0.286275, 0.521569, 0.65098, 422436.55859375, 0.337255, 0.592157, 0.701961, 439266.9609375, 0.388235, 0.654902, 0.74902, 456097.36328125, 0.466667, 0.737255, 0.819608, 472927.765625, 0.572549, 0.819608, 0.878431, 489758.16796875, 0.654902, 0.866667, 0.909804, 506588.5703125, 0.752941, 0.917647, 0.941176, 523418.97265625, 0.823529, 0.956863, 0.968627, 540249.375, 0.941176, 0.984314, 0.988235, 540249.375, 0.988235, 0.960784, 0.901961, 551020.8325, 0.988235, 0.945098, 0.85098, 561792.29, 0.980392, 0.898039, 0.784314, 573910.1796875, 0.968627, 0.835294, 0.698039, 590740.58203125, 0.94902, 0.733333, 0.588235, 607570.984375, 0.929412, 0.65098, 0.509804, 624401.38671875, 0.909804, 0.564706, 0.435294, 641231.7890625, 0.878431, 0.458824, 0.352941, 658062.19140625, 0.839216, 0.388235, 0.286275, 674892.59375, 0.760784, 0.294118, 0.211765, 691722.99609375, 0.701961, 0.211765, 0.168627, 708553.3984375, 0.65098, 0.156863, 0.129412, 725383.80078125, 0.6, 0.094118, 0.094118, 742214.203125, 0.54902, 0.066667, 0.098039, 759044.60546875, 0.501961, 0.05098, 0.12549, 775875.0078125, 0.45098, 0.054902, 0.172549, 792705.41015625, 0.4, 0.054902, 0.192157, 809535.8125, 0.34902, 0.070588, 0.211765]
vtkBlockColorsLUT.ColorSpace = 'Lab'
vtkBlockColorsLUT.NanColor = [0.25, 0.0, 0.0]
vtkBlockColorsLUT.Discretize = 0
vtkBlockColorsLUT.Annotations = ['0', '0', '1', '1', '2', '2', '3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8', '9', '9', '10', '10', '11', '11']
vtkBlockColorsLUT.ActiveAnnotatedValues = ['0', '3']
vtkBlockColorsLUT.IndexedColors = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.63, 0.63, 1.0, 0.67, 0.5, 0.33, 1.0, 0.5, 0.75, 0.53, 0.35, 0.7, 1.0, 0.75, 0.5]

# get opacity transfer function/opacity map for 'vtkBlockColors'
vtkBlockColorsPWF = GetOpacityTransferFunction('vtkBlockColors')
vtkBlockColorsPWF.Points = [270962.9375, 0.0, 0.5, 0.0, 809535.8125, 1.0, 0.5, 0.0]

# rename source object
RenameSource('foam_file', combustorfoam)

# change representation type
combustorfoamDisplay.SetRepresentationType('Surface With Edges')

# change representation type
combustorfoamDisplay.SetRepresentationType('Feature Edges')

# turn off scalar coloring
ColorBy(combustorfoamDisplay, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(vtkBlockColorsLUT, renderView1)

# Properties modified on combustorfoam
combustorfoam.MeshRegions = ['fuel_inlet', 'inlet', 'outlet', 'splitter']
combustorfoam.CellArrays = []
combustorfoam.LagrangianArrays = []

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(combustor2Dwf_)

# create a new 'Contour'
contour1 = Contour(Input=combustor2Dwf_)

# Properties modified on contour1
contour1.Isosurfaces = [0.0, 0.005000000000000001, 0.010000000000000002, 0.015, 0.020000000000000004, 0.025, 0.03, 0.034999999999999996, 0.04000000000000001, 0.045000000000000005, 0.05, 0.05500000000000001, 0.06, 0.065, 0.06999999999999999, 0.07500000000000001, 0.08000000000000002, 0.085, 0.09000000000000001, 0.095, 0.1]

# show data in view
contour1Display = Show(contour1, renderView1)

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'

# hide data in view
Hide(combustor2Dwf_, renderView1)

# show color bar/color legend
contour1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# change representation type
contour1Display.SetRepresentationType('Wireframe')

# Properties modified on contour1Display
contour1Display.LineWidth = 5.0

# Properties modified on contour1Display
contour1Display.LineWidth = 3.0

# Properties modified on contour1Display
contour1Display.LineWidth = 5.0

# rename source object
RenameSource('fuel_contour', contour1)

# set active source
SetActiveSource(combustor2Dwf_)

# set active source
SetActiveSource(combustor2Dwf_)

# show data in view
combustor2Dwf_Display = Show(combustor2Dwf_, renderView1)

# show color bar/color legend
combustor2Dwf_Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(combustor2Dwf_, renderView1)

# set active source
SetActiveSource(combustorfoam)

# Properties modified on combustorfoam
combustorfoam.MeshRegions = ['back', 'fuel_inlet', 'inlet', 'outlet', 'splitter']

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(combustor2Dwf_)

# show data in view
combustor2Dwf_Display = Show(combustor2Dwf_, renderView1)

# show color bar/color legend
combustor2Dwf_Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(combustor2Dwf_, renderView1)

# create a new 'Legacy VTK Reader'
combustor2Dwf__1 = LegacyVTKReader(FileNames=['/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/VTK/wallFilmRegion/combustor2D-wf_0.vtk', '/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/VTK/wallFilmRegion/combustor2D-wf_454.vtk', '/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/VTK/wallFilmRegion/combustor2D-wf_909.vtk', '/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/VTK/wallFilmRegion/combustor2D-wf_1399.vtk', '/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/VTK/wallFilmRegion/combustor2D-wf_2135.vtk', '/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/VTK/wallFilmRegion/combustor2D-wf_2977.vtk', '/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/VTK/wallFilmRegion/combustor2D-wf_3845.vtk', '/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/VTK/wallFilmRegion/combustor2D-wf_4708.vtk', '/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/VTK/wallFilmRegion/combustor2D-wf_5532.vtk', '/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/VTK/wallFilmRegion/combustor2D-wf_6279.vtk', '/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/VTK/wallFilmRegion/combustor2D-wf_6938.vtk'])

# show data in view
combustor2Dwf__1Display = Show(combustor2Dwf__1, renderView1)

# trace defaults for the display properties.
combustor2Dwf__1Display.Representation = 'Surface'

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(combustor2Dwf__1Display, ('POINTS', 'delta'))

# rescale color and/or opacity maps used to include current data range
combustor2Dwf__1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
combustor2Dwf__1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'delta'
deltaLUT = GetColorTransferFunction('delta')
deltaLUT.RGBPoints = [0.0, 0.0, 0.0, 0.34902, 3.674316677336816e-40, 0.039216, 0.062745, 0.380392, 7.348633354673633e-40, 0.062745, 0.117647, 0.411765, 1.1022950032010449e-39, 0.090196, 0.184314, 0.45098, 1.4697266709347265e-39, 0.12549, 0.262745, 0.501961, 1.8371583386684082e-39, 0.160784, 0.337255, 0.541176, 2.2045900064020898e-39, 0.2, 0.396078, 0.568627, 2.5720216741357714e-39, 0.239216, 0.454902, 0.6, 2.939453341869453e-39, 0.286275, 0.521569, 0.65098, 3.306885009603135e-39, 0.337255, 0.592157, 0.701961, 3.6743166773368163e-39, 0.388235, 0.654902, 0.74902, 4.041748345070498e-39, 0.466667, 0.737255, 0.819608, 4.4091800128041796e-39, 0.572549, 0.819608, 0.878431, 4.776611680537861e-39, 0.654902, 0.866667, 0.909804, 5.144043348271543e-39, 0.752941, 0.917647, 0.941176, 5.5114750160052245e-39, 0.823529, 0.956863, 0.968627, 5.878906683738906e-39, 0.988235, 0.960784, 0.901961, 5.878906683738906e-39, 0.941176, 0.984314, 0.988235, 6.114062951088463e-39, 0.988235, 0.945098, 0.85098, 6.349219218438019e-39, 0.980392, 0.898039, 0.784314, 6.61377001920627e-39, 0.968627, 0.835294, 0.698039, 6.981201686939951e-39, 0.94902, 0.733333, 0.588235, 7.348633354673633e-39, 0.929412, 0.65098, 0.509804, 7.716065022407314e-39, 0.909804, 0.564706, 0.435294, 8.083496690140996e-39, 0.878431, 0.458824, 0.352941, 8.450928357874678e-39, 0.839216, 0.388235, 0.286275, 8.818360025608359e-39, 0.760784, 0.294118, 0.211765, 9.185791693342041e-39, 0.701961, 0.211765, 0.168627, 9.553223361075722e-39, 0.65098, 0.156863, 0.129412, 9.920655028809404e-39, 0.6, 0.094118, 0.094118, 1.0288086696543086e-38, 0.54902, 0.066667, 0.098039, 1.0655518364276767e-38, 0.501961, 0.05098, 0.12549, 1.1022950032010449e-38, 0.45098, 0.054902, 0.172549, 1.1390381699744131e-38, 0.4, 0.054902, 0.192157, 1.1757813367477812e-38, 0.34902, 0.070588, 0.211765]
deltaLUT.ColorSpace = 'Lab'
deltaLUT.NanColor = [0.25, 0.0, 0.0]
deltaLUT.Discretize = 0
deltaLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'delta'
deltaPWF = GetOpacityTransferFunction('delta')
deltaPWF.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
deltaPWF.ScalarRangeInitialized = 1

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
deltaLUT.ApplyPreset('Black, Blue and White', True)

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 0.09999999403953552, 1.613534515632741]
renderView1.CameraFocalPoint = [0.0, 0.09999999403953552, 0.0]
renderView1.CameraParallelScale = 0.41761346257602433

# save screenshot
SaveScreenshot('/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/paraviewPostProcessing/Images/contour_fuel.png', renderView1, ImageResolution=[4584, 6360],
    TransparentBackground=1)

# create a new 'Legacy VTK Reader'
sprayCloud_ = LegacyVTKReader(FileNames=['/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/VTK/lagrangian/sprayCloud/sprayCloud_0.vtk', '/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/VTK/lagrangian/sprayCloud/sprayCloud_454.vtk', '/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/VTK/lagrangian/sprayCloud/sprayCloud_909.vtk', '/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/VTK/lagrangian/sprayCloud/sprayCloud_1399.vtk', '/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/VTK/lagrangian/sprayCloud/sprayCloud_2135.vtk', '/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/VTK/lagrangian/sprayCloud/sprayCloud_2977.vtk', '/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/VTK/lagrangian/sprayCloud/sprayCloud_3845.vtk', '/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/VTK/lagrangian/sprayCloud/sprayCloud_4708.vtk', '/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/VTK/lagrangian/sprayCloud/sprayCloud_5532.vtk', '/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/VTK/lagrangian/sprayCloud/sprayCloud_6279.vtk', '/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/VTK/lagrangian/sprayCloud/sprayCloud_6938.vtk'])

# show data in view
sprayCloud_Display = Show(sprayCloud_, renderView1)

# trace defaults for the display properties.
sprayCloud_Display.Representation = 'Surface'

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Glyph'
glyph1 = Glyph(Input=sprayCloud_,
    GlyphType='Arrow')

# Properties modified on glyph1
glyph1.GlyphType = 'Sphere'
glyph1.ScaleArray = ['POINTS', 'No scale array']
glyph1.ScaleFactor = 0.01
glyph1.GlyphMode = 'All Points'

# show data in view
glyph1Display = Show(glyph1, renderView1)

# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(glyph1Display, ('POINTS', 'd'))

# rescale color and/or opacity maps used to include current data range
glyph1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'd'
dLUT = GetColorTransferFunction('d')
dLUT.RGBPoints = [2.9202335554145975e-06, 0.0, 0.0, 0.34902, 7.475895280606437e-06, 0.039216, 0.062745, 0.380392, 1.2031557005798277e-05, 0.062745, 0.117647, 0.411765, 1.6587218730990116e-05, 0.090196, 0.184314, 0.45098, 2.1142880456181956e-05, 0.12549, 0.262745, 0.501961, 2.5698542181373796e-05, 0.160784, 0.337255, 0.541176, 3.0254203906565635e-05, 0.2, 0.396078, 0.568627, 3.4809865631757475e-05, 0.239216, 0.454902, 0.6, 3.9365527356949315e-05, 0.286275, 0.521569, 0.65098, 4.3921189082141154e-05, 0.337255, 0.592157, 0.701961, 4.8476850807332994e-05, 0.388235, 0.654902, 0.74902, 5.3032512532524834e-05, 0.466667, 0.737255, 0.819608, 5.758817425771667e-05, 0.572549, 0.819608, 0.878431, 6.214383598290851e-05, 0.654902, 0.866667, 0.909804, 6.669949770810035e-05, 0.752941, 0.917647, 0.941176, 7.125515943329219e-05, 0.823529, 0.956863, 0.968627, 7.581082115848403e-05, 0.988235, 0.960784, 0.901961, 7.581082115848403e-05, 0.941176, 0.984314, 0.988235, 7.872644466260682e-05, 0.988235, 0.945098, 0.85098, 8.164206816672959e-05, 0.980392, 0.898039, 0.784314, 8.492214460886771e-05, 0.968627, 0.835294, 0.698039, 8.947780633405955e-05, 0.94902, 0.733333, 0.588235, 9.403346805925139e-05, 0.929412, 0.65098, 0.509804, 9.858912978444323e-05, 0.909804, 0.564706, 0.435294, 0.00010314479150963507, 0.878431, 0.458824, 0.352941, 0.00010770045323482691, 0.839216, 0.388235, 0.286275, 0.00011225611496001875, 0.760784, 0.294118, 0.211765, 0.00011681177668521059, 0.701961, 0.211765, 0.168627, 0.00012136743841040243, 0.65098, 0.156863, 0.129412, 0.00012592310013559427, 0.6, 0.094118, 0.094118, 0.0001304787618607861, 0.54902, 0.066667, 0.098039, 0.00013503442358597795, 0.501961, 0.05098, 0.12549, 0.0001395900853111698, 0.45098, 0.054902, 0.172549, 0.00014414574703636163, 0.4, 0.054902, 0.192157, 0.00014870140876155347, 0.34902, 0.070588, 0.211765]
dLUT.ColorSpace = 'Lab'
dLUT.NanColor = [0.25, 0.0, 0.0]
dLUT.Discretize = 0
dLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'd'
dPWF = GetOpacityTransferFunction('d')
dPWF.Points = [2.9202335554145975e-06, 0.0, 0.5, 0.0, 0.00014870140876155347, 1.0, 0.5, 0.0]
dPWF.ScalarRangeInitialized = 1

# Properties modified on glyph1
glyph1.ScaleFactor = 0.001

# update the view to ensure updated data information
renderView1.Update()

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
dLUT.ApplyPreset('X Ray', True)

#change interaction mode for render view
renderView1.InteractionMode = '2D'

#change interaction mode for render view
renderView1.InteractionMode = '3D'

# set active source
SetActiveSource(contour1)

# Properties modified on contour1Display
contour1Display.LineWidth = 3.0

# Properties modified on contour1Display
contour1Display.LineWidth = 1.0

# Properties modified on contour1Display
contour1Display.LineWidth = 2.0

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 0.09999999403953552, 1.613534515632741]
renderView1.CameraFocalPoint = [0.0, 0.09999999403953552, 0.0]
renderView1.CameraParallelScale = 0.41761346257602433

# save screenshot
SaveScreenshot('/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/paraviewPostProcessing/Images/contour_fuel_with_parcels02.png', renderView1, ImageResolution=[4584, 6360],
    TransparentBackground=1)

# set active source
SetActiveSource(combustor2Dwf__1)

# rename source object
RenameSource('wallFilmRegion', combustor2Dwf__1)

# create a new 'Plot Data'
plotData1 = PlotData(Input=combustor2Dwf__1)

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')
# uncomment following to set a specific view size
# lineChartView1.ViewSize = [400, 400]

# show data in view
plotData1Display = Show(plotData1, lineChartView1)

# get layout
layout1 = GetLayoutByName("Layout #1")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# destroy lineChartView1
Delete(lineChartView1)
del lineChartView1

# close an empty frame
layout1.Collapse(2)

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(combustor2Dwf__1)

# destroy plotData1
Delete(plotData1)
del plotData1

# create a new 'Plot Data'
plotData1 = PlotData(Input=combustor2Dwf__1)

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')
# uncomment following to set a specific view size
# lineChartView1.ViewSize = [400, 400]

# show data in view
plotData1Display = Show(plotData1, lineChartView1)

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = []
plotData1Display.SeriesColor = ['alpha', '0', '0', '0', 'contactForce:contactAngle_X', '0.889998', '0.100008', '0.110002', 'contactForce:contactAngle_Y', '0.220005', '0.489998', '0.719997', 'contactForce:contactAngle_Z', '0.300008', '0.689998', '0.289998', 'contactForce:contactAngle_Magnitude', '0.6', '0.310002', '0.639994', 'coverage', '1', '0.500008', '0', 'Cp', '0.650004', '0.340002', '0.160006', 'delta', '0', '0', '0', 'kappa', '0.889998', '0.100008', '0.110002', 'mu', '0.220005', '0.489998', '0.719997', 'rho', '0.300008', '0.689998', '0.289998', 'sigma', '0.6', '0.310002', '0.639994', 'T', '1', '0.500008', '0', 'U_X', '0.650004', '0.340002', '0.160006', 'U_Y', '0', '0', '0', 'U_Z', '0.889998', '0.100008', '0.110002', 'U_Magnitude', '0.220005', '0.489998', '0.719997', 'Points_X', '0.300008', '0.689998', '0.289998', 'Points_Y', '0.6', '0.310002', '0.639994', 'Points_Z', '1', '0.500008', '0', 'Points_Magnitude', '0.650004', '0.340002', '0.160006']
plotData1Display.SeriesPlotCorner = ['Cp', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'alpha', '0', 'contactForce:contactAngle_Magnitude', '0', 'contactForce:contactAngle_X', '0', 'contactForce:contactAngle_Y', '0', 'contactForce:contactAngle_Z', '0', 'coverage', '0', 'delta', '0', 'kappa', '0', 'mu', '0', 'rho', '0', 'sigma', '0']
plotData1Display.SeriesLineStyle = ['Cp', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'T', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'alpha', '1', 'contactForce:contactAngle_Magnitude', '1', 'contactForce:contactAngle_X', '1', 'contactForce:contactAngle_Y', '1', 'contactForce:contactAngle_Z', '1', 'coverage', '1', 'delta', '1', 'kappa', '1', 'mu', '1', 'rho', '1', 'sigma', '1']
plotData1Display.SeriesLineThickness = ['Cp', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'T', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'alpha', '2', 'contactForce:contactAngle_Magnitude', '2', 'contactForce:contactAngle_X', '2', 'contactForce:contactAngle_Y', '2', 'contactForce:contactAngle_Z', '2', 'coverage', '2', 'delta', '2', 'kappa', '2', 'mu', '2', 'rho', '2', 'sigma', '2']
plotData1Display.SeriesMarkerStyle = ['Cp', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'alpha', '0', 'contactForce:contactAngle_Magnitude', '0', 'contactForce:contactAngle_X', '0', 'contactForce:contactAngle_Y', '0', 'contactForce:contactAngle_Z', '0', 'coverage', '0', 'delta', '0', 'kappa', '0', 'mu', '0', 'rho', '0', 'sigma', '0']

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = ['alpha', 'contactForce:contactAngle_X', 'contactForce:contactAngle_Y', 'contactForce:contactAngle_Z', 'contactForce:contactAngle_Magnitude', 'coverage', 'Cp', 'delta', 'kappa', 'mu', 'rho', 'sigma', 'T', 'U_X', 'U_Y', 'U_Z', 'U_Magnitude', 'Points_X', 'Points_Y', 'Points_Z', 'Points_Magnitude']

# save data
SaveData('/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/paraviewPostProcessing/Data/wallFilm02.txt', proxy=plotData1, Precision=6,
    UseScientificNotation=1)

# set active view
SetActiveView(renderView1)

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 0.09999999403953552, 1.613534515632741]
renderView1.CameraFocalPoint = [0.0, 0.09999999403953552, 0.0]
renderView1.CameraParallelScale = 0.41761346257602433

# save screenshot
SaveScreenshot('/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/paraviewPostProcessing/Images/contour_fuel_with_parcels02.png', renderView1, ImageResolution=[5704, 6360],
    TransparentBackground=1)

# hide data in view
Hide(sprayCloud_, renderView1)

# hide data in view
Hide(glyph1, renderView1)

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 0.09999999403953552, 1.613534515632741]
renderView1.CameraFocalPoint = [0.0, 0.09999999403953552, 0.0]
renderView1.CameraParallelScale = 0.41761346257602433

# save screenshot
SaveScreenshot('/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/paraviewPostProcessing/Images/contour_fuel02.png', renderView1, ImageResolution=[5704, 6360],
    TransparentBackground=1)

# Properties modified on animationScene1
animationScene1.AnimationTime = 4.0

# Properties modified on timeKeeper1
timeKeeper1.Time = 4.0

# set active source
SetActiveSource(combustor2Dwf__1)

# Rescale transfer function
deltaLUT.RescaleTransferFunction(0.0, 0.00020275726274121553)

# Rescale transfer function
deltaPWF.RescaleTransferFunction(0.0, 0.00020275726274121553)

# set active source
SetActiveSource(contour1)

# Rescale transfer function
c7H16LUT.RescaleTransferFunction(0.004999999888241291, 0.10000000149011612)

# Rescale transfer function
c7H16PWF.RescaleTransferFunction(0.004999999888241291, 0.10000000149011612)

# Properties modified on animationScene1
animationScene1.AnimationTime = 2.0

# Properties modified on timeKeeper1
timeKeeper1.Time = 2.0

# set active source
SetActiveSource(sprayCloud_)

# show data in view
sprayCloud_Display = Show(sprayCloud_, renderView1)

# hide data in view
Hide(sprayCloud_, renderView1)

# set active source
SetActiveSource(glyph1)

# show data in view
glyph1Display = Show(glyph1, renderView1)

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# Rescale transfer function
dLUT.RescaleTransferFunction(2.0881580553577805e-07, 0.00014993216609582305)

# Rescale transfer function
dPWF.RescaleTransferFunction(2.0881580553577805e-07, 0.00014993216609582305)

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 0.09999999403953552, 1.613534515632741]
renderView1.CameraFocalPoint = [0.0, 0.09999999403953552, 0.0]
renderView1.CameraParallelScale = 0.41761346257602433

# save screenshot
SaveScreenshot('/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/paraviewPostProcessing/Images/contour_fuel_with_parcels02.png', renderView1, ImageResolution=[5704, 6360],
    TransparentBackground=1)

# hide data in view
Hide(glyph1, renderView1)

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 0.09999999403953552, 1.613534515632741]
renderView1.CameraFocalPoint = [0.0, 0.09999999403953552, 0.0]
renderView1.CameraParallelScale = 0.41761346257602433

# save screenshot
SaveScreenshot('/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/paraviewPostProcessing/Images/contour_fuel02.png', renderView1, ImageResolution=[5704, 6360],
    TransparentBackground=1)

# show data in view
glyph1Display = Show(glyph1, renderView1)

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# Properties modified on animationScene1
animationScene1.AnimationTime = 4.0

# Properties modified on timeKeeper1
timeKeeper1.Time = 4.0

# set active view
SetActiveView(lineChartView1)

# save data
SaveData('/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/paraviewPostProcessing/Data/wallFilm04.txt', proxy=glyph1, Precision=6,
    UseScientificNotation=1)

# set active view
SetActiveView(renderView1)

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 0.09999999403953552, 1.613534515632741]
renderView1.CameraFocalPoint = [0.0, 0.09999999403953552, 0.0]
renderView1.CameraParallelScale = 0.41761346257602433

# save screenshot
SaveScreenshot('/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/paraviewPostProcessing/Images/contour_fuel_with_parcels04.png', renderView1, ImageResolution=[5704, 6360],
    TransparentBackground=1)

# hide data in view
Hide(glyph1, renderView1)

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 0.09999999403953552, 1.613534515632741]
renderView1.CameraFocalPoint = [0.0, 0.09999999403953552, 0.0]
renderView1.CameraParallelScale = 0.41761346257602433

# save screenshot
SaveScreenshot('/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/paraviewPostProcessing/Images/contour_fuel04.png', renderView1, ImageResolution=[5704, 6360],
    TransparentBackground=1)

# Properties modified on animationScene1
animationScene1.AnimationTime = 5.0

# Properties modified on timeKeeper1
timeKeeper1.Time = 5.0

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 0.09999999403953552, 1.613534515632741]
renderView1.CameraFocalPoint = [0.0, 0.09999999403953552, 0.0]
renderView1.CameraParallelScale = 0.41761346257602433

# save screenshot
SaveScreenshot('/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/paraviewPostProcessing/Images/contour_fuel05.png', renderView1, ImageResolution=[5704, 6360],
    TransparentBackground=1)

# show data in view
glyph1Display = Show(glyph1, renderView1)

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 0.09999999403953552, 1.613534515632741]
renderView1.CameraFocalPoint = [0.0, 0.09999999403953552, 0.0]
renderView1.CameraParallelScale = 0.41761346257602433

# save screenshot
SaveScreenshot('/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/paraviewPostProcessing/Images/contour_fuel_with_parcels05.png', renderView1, ImageResolution=[5704, 6360],
    TransparentBackground=1)

# set active view
SetActiveView(lineChartView1)

# save data
SaveData('/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/paraviewPostProcessing/Data/wallFilm05.txt', proxy=glyph1, Precision=6,
    UseScientificNotation=1)

# set active view
SetActiveView(renderView1)

# Properties modified on animationScene1
animationScene1.AnimationTime = 8.0

# Properties modified on timeKeeper1
timeKeeper1.Time = 8.0

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 0.09999999403953552, 1.613534515632741]
renderView1.CameraFocalPoint = [0.0, 0.09999999403953552, 0.0]
renderView1.CameraParallelScale = 0.41761346257602433

# save screenshot
SaveScreenshot('/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/paraviewPostProcessing/Images/contour_fuel_with_parcels08.png', renderView1, ImageResolution=[5704, 6360],
    TransparentBackground=1)

# hide data in view
Hide(glyph1, renderView1)

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 0.09999999403953552, 1.613534515632741]
renderView1.CameraFocalPoint = [0.0, 0.09999999403953552, 0.0]
renderView1.CameraParallelScale = 0.41761346257602433

# save screenshot
SaveScreenshot('/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/paraviewPostProcessing/Images/contour_fuel08.png', renderView1, ImageResolution=[5704, 6360],
    TransparentBackground=1)

# set active view
SetActiveView(lineChartView1)

# save data
SaveData('/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/paraviewPostProcessing/Data/wallFilm08.txt', proxy=glyph1, Precision=6,
    UseScientificNotation=1)

# set active view
SetActiveView(renderView1)

# show data in view
glyph1Display = Show(glyph1, renderView1)

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(combustor2Dwf__1, renderView1)

# hide data in view
Hide(combustorfoam, renderView1)

# hide data in view
Hide(contour1, renderView1)

# set active view
SetActiveView(lineChartView1)

# destroy lineChartView1
Delete(lineChartView1)
del lineChartView1

# close an empty frame
layout1.Collapse(2)

# set active view
SetActiveView(renderView1)

# create a new 'Plot Data'
plotData2 = PlotData(Input=glyph1)

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')
# uncomment following to set a specific view size
# lineChartView1.ViewSize = [400, 400]

# show data in view
plotData2Display = Show(plotData2, lineChartView1)

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# set active view
SetActiveView(renderView1)

# set active view
SetActiveView(lineChartView1)

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(glyph1)

# hide data in view
Hide(plotData2, lineChartView1)

# destroy plotData2
Delete(plotData2)
del plotData2

# create a new 'Plot Data'
plotData2 = PlotData(Input=glyph1)

# set active view
SetActiveView(lineChartView1)

# show data in view
plotData2Display = Show(plotData2, lineChartView1)

# update the view to ensure updated data information
lineChartView1.Update()

# Properties modified on plotData2Display
plotData2Display.SeriesVisibility = ['active', 'age', 'd', 'd0', 'dTarget', 'injector', 'KHindex', 'liquidCore', 'mass0', 'ms', 'mu', 'Normals_Magnitude', 'nParticle', 'origId', 'origProcId', 'position0_Magnitude', 'rho', 'sigma', 'T', 'tc', 'tMom', 'tTurb', 'typeId', 'U_Magnitude', 'user', 'UTurb_Magnitude', 'y', 'YC7H16(l)', 'yDot']
plotData2Display.SeriesColor = ['active', '0', '0', '0', 'age', '0.889998', '0.100008', '0.110002', 'Cp', '0.220005', '0.489998', '0.719997', 'd', '0.300008', '0.689998', '0.289998', 'd0', '0.6', '0.310002', '0.639994', 'dTarget', '1', '0.500008', '0', 'injector', '0.650004', '0.340002', '0.160006', 'KHindex', '0', '0', '0', 'liquidCore', '0.889998', '0.100008', '0.110002', 'mass0', '0.220005', '0.489998', '0.719997', 'ms', '0.300008', '0.689998', '0.289998', 'mu', '0.6', '0.310002', '0.639994', 'Normals_X', '1', '0.500008', '0', 'Normals_Y', '0.650004', '0.340002', '0.160006', 'Normals_Z', '0', '0', '0', 'Normals_Magnitude', '0.889998', '0.100008', '0.110002', 'nParticle', '0.220005', '0.489998', '0.719997', 'origId', '0.300008', '0.689998', '0.289998', 'origProcId', '0.6', '0.310002', '0.639994', 'position0_X', '1', '0.500008', '0', 'position0_Y', '0.650004', '0.340002', '0.160006', 'position0_Z', '0', '0', '0', 'position0_Magnitude', '0.889998', '0.100008', '0.110002', 'rho', '0.220005', '0.489998', '0.719997', 'sigma', '0.300008', '0.689998', '0.289998', 'T', '0.6', '0.310002', '0.639994', 'tc', '1', '0.500008', '0', 'tMom', '0.650004', '0.340002', '0.160006', 'tTurb', '0', '0', '0', 'typeId', '0.889998', '0.100008', '0.110002', 'U_X', '0.220005', '0.489998', '0.719997', 'U_Y', '0.300008', '0.689998', '0.289998', 'U_Z', '0.6', '0.310002', '0.639994', 'U_Magnitude', '1', '0.500008', '0', 'user', '0.650004', '0.340002', '0.160006', 'UTurb_X', '0', '0', '0', 'UTurb_Y', '0.889998', '0.100008', '0.110002', 'UTurb_Z', '0.220005', '0.489998', '0.719997', 'UTurb_Magnitude', '0.300008', '0.689998', '0.289998', 'y', '0.6', '0.310002', '0.639994', 'YC7H16(l)', '1', '0.500008', '0', 'yDot', '0.650004', '0.340002', '0.160006', 'Points_X', '0', '0', '0', 'Points_Y', '0.889998', '0.100008', '0.110002', 'Points_Z', '0.220005', '0.489998', '0.719997', 'Points_Magnitude', '0.300008', '0.689998', '0.289998']
plotData2Display.SeriesPlotCorner = ['Cp', '0', 'KHindex', '0', 'Normals_Magnitude', '0', 'Normals_X', '0', 'Normals_Y', '0', 'Normals_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'UTurb_Magnitude', '0', 'UTurb_X', '0', 'UTurb_Y', '0', 'UTurb_Z', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'YC7H16(l)', '0', 'active', '0', 'age', '0', 'd', '0', 'd0', '0', 'dTarget', '0', 'injector', '0', 'liquidCore', '0', 'mass0', '0', 'ms', '0', 'mu', '0', 'nParticle', '0', 'origId', '0', 'origProcId', '0', 'position0_Magnitude', '0', 'position0_X', '0', 'position0_Y', '0', 'position0_Z', '0', 'rho', '0', 'sigma', '0', 'tMom', '0', 'tTurb', '0', 'tc', '0', 'typeId', '0', 'user', '0', 'y', '0', 'yDot', '0']
plotData2Display.SeriesLineStyle = ['Cp', '1', 'KHindex', '1', 'Normals_Magnitude', '1', 'Normals_X', '1', 'Normals_Y', '1', 'Normals_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'T', '1', 'UTurb_Magnitude', '1', 'UTurb_X', '1', 'UTurb_Y', '1', 'UTurb_Z', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'YC7H16(l)', '1', 'active', '1', 'age', '1', 'd', '1', 'd0', '1', 'dTarget', '1', 'injector', '1', 'liquidCore', '1', 'mass0', '1', 'ms', '1', 'mu', '1', 'nParticle', '1', 'origId', '1', 'origProcId', '1', 'position0_Magnitude', '1', 'position0_X', '1', 'position0_Y', '1', 'position0_Z', '1', 'rho', '1', 'sigma', '1', 'tMom', '1', 'tTurb', '1', 'tc', '1', 'typeId', '1', 'user', '1', 'y', '1', 'yDot', '1']
plotData2Display.SeriesLineThickness = ['Cp', '2', 'KHindex', '2', 'Normals_Magnitude', '2', 'Normals_X', '2', 'Normals_Y', '2', 'Normals_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'T', '2', 'UTurb_Magnitude', '2', 'UTurb_X', '2', 'UTurb_Y', '2', 'UTurb_Z', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'YC7H16(l)', '2', 'active', '2', 'age', '2', 'd', '2', 'd0', '2', 'dTarget', '2', 'injector', '2', 'liquidCore', '2', 'mass0', '2', 'ms', '2', 'mu', '2', 'nParticle', '2', 'origId', '2', 'origProcId', '2', 'position0_Magnitude', '2', 'position0_X', '2', 'position0_Y', '2', 'position0_Z', '2', 'rho', '2', 'sigma', '2', 'tMom', '2', 'tTurb', '2', 'tc', '2', 'typeId', '2', 'user', '2', 'y', '2', 'yDot', '2']
plotData2Display.SeriesMarkerStyle = ['Cp', '0', 'KHindex', '0', 'Normals_Magnitude', '0', 'Normals_X', '0', 'Normals_Y', '0', 'Normals_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'T', '0', 'UTurb_Magnitude', '0', 'UTurb_X', '0', 'UTurb_Y', '0', 'UTurb_Z', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'YC7H16(l)', '0', 'active', '0', 'age', '0', 'd', '0', 'd0', '0', 'dTarget', '0', 'injector', '0', 'liquidCore', '0', 'mass0', '0', 'ms', '0', 'mu', '0', 'nParticle', '0', 'origId', '0', 'origProcId', '0', 'position0_Magnitude', '0', 'position0_X', '0', 'position0_Y', '0', 'position0_Z', '0', 'rho', '0', 'sigma', '0', 'tMom', '0', 'tTurb', '0', 'tc', '0', 'typeId', '0', 'user', '0', 'y', '0', 'yDot', '0']

# Properties modified on plotData2Display
plotData2Display.SeriesVisibility = ['active', 'age', 'd', 'd0', 'dTarget', 'injector', 'liquidCore', 'mass0', 'ms', 'mu', 'Normals_Magnitude', 'nParticle', 'origId', 'origProcId', 'position0_Magnitude', 'rho', 'sigma', 'T', 'tc', 'tMom', 'tTurb', 'typeId', 'U_Magnitude', 'user', 'UTurb_Magnitude', 'y', 'YC7H16(l)', 'yDot']

# save data
SaveData('/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/paraviewPostProcessing/Data/particleCloudData08.txt', proxy=plotData2, Precision=6,
    UseScientificNotation=1)

# set active view
SetActiveView(renderView1)

# Properties modified on animationScene1
animationScene1.AnimationTime = 5.0

# Properties modified on timeKeeper1
timeKeeper1.Time = 5.0

# set active view
SetActiveView(lineChartView1)

# set active view
SetActiveView(renderView1)

# set active view
SetActiveView(lineChartView1)

# save data
SaveData('/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/paraviewPostProcessing/Data/particleCloudData05.txt', proxy=plotData2, Precision=6,
    UseScientificNotation=1)

# Properties modified on animationScene1
animationScene1.AnimationTime = 2.0

# Properties modified on timeKeeper1
timeKeeper1.Time = 2.0

# set active view
SetActiveView(renderView1)

# set active view
SetActiveView(lineChartView1)

# save data
SaveData('/home/edo20/Piscaglia/Shared_docker_folder/Shared_CTTP/testEdo/Labs/Lab0506/combustor2D-wf/paraviewPostProcessing/Data/particleCloudData02.txt', proxy=plotData2, Precision=6,
    UseScientificNotation=1)

# set active view
SetActiveView(renderView1)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.01421880104562484, 0.09999999403953552, 1.6134718649034476]
renderView1.CameraFocalPoint = [0.0, 0.09999999403953552, 0.0]
renderView1.CameraParallelScale = 0.41761346257602433

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).