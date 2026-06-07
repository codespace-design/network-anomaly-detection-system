import os
import joblib
from django.shortcuts import render
from django.conf import settings

# Load model and scaler once
MODEL_DIR = os.path.join(settings.BASE_DIR, 'models')
SCALER_PATH = os.path.join(MODEL_DIR, 'scaler.pkl')
MODEL_PATH = os.path.join(MODEL_DIR, 'knn_ids_model.pkl')

try:
    scaler = joblib.load(SCALER_PATH)
    model = joblib.load(MODEL_PATH)
except Exception as e:
    scaler = None
    model = None
    print(f"Error loading models: {e}")

FEATURE_NAMES = [
    "duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes", 
    "count", "srv_count", "same_srv_rate", "diff_srv_rate", "serror_rate", 
    "srv_serror_rate", "rerror_rate", "srv_rerror_rate", "dst_host_count", "dst_host_srv_count"
]

def index(request):
    feature_data = [{'name': f, 'label': f.replace('_', ' ').title()} for f in FEATURE_NAMES]
    context = {'features': feature_data}
    
    if request.method == 'POST':
        if not scaler or not model:
            context['error'] = 'Model or Scaler not loaded properly.'
            return render(request, 'anomaly_detector/index.html', context)
            
        try:
            # Extract features from POST request
            input_data = []
            for f in FEATURE_NAMES:
                val = request.POST.get(f, 0)
                input_data.append(float(val))
            
            # Scale data
            scaled_data = scaler.transform([input_data])
            
            # Predict (0 -> Normal, 1 -> Anomaly)
            prediction = model.predict(scaled_data)[0]
            
            context['prediction'] = 'Anomaly' if prediction == 1.0 else 'Normal'
            context['prediction_raw'] = prediction
            
            # Pass back input values to repopulate the form
            for f_dict in context['features']:
                f_dict['value'] = request.POST.get(f_dict['name'], '0')
            
        except Exception as e:
            context['error'] = f'Error during prediction: {str(e)}'
            
    return render(request, 'anomaly_detector/index.html', context)
