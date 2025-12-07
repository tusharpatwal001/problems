### Quantization

1. Full Precission/ Half Precission -- Data -> Weights and Parameters
2. Calibration -- Model Quantization -> Problems
3. Modes of Quantization

   - Post Training Quantization
   - Quantization Aware Training

4. Quantization -- Conversion from higher memory format to a lower memory format

![Quantization](.\data\quantization.png)

- Converting `FP 32 bit` --> `FP 16 bit` or `FP 8 bit`
- FP stands for Full Precision (like Converting `4 bytes` int to `1 byte` for reducing the model size)
