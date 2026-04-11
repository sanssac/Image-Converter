import streamlit as st
from PIL import Image
from core.converter import jpeg_to_png, png_to_jpeg
import tempfile
import os

st.set_page_config(
    page_title="Image Converter",
    page_icon="🖼️",
    layout="centered"
)

st.title("🖼️ Image Converter")
st.write("Convert images between JPEG and PNG formats instantly.")

uploaded = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded:
    st.image(uploaded, caption="Preview", width=300)

    file_size = len(uploaded.getvalue()) / 1024
    st.info(f"📄 File: {uploaded.name} | 📦 Size: {file_size:.1f} KB")

    format_choice = st.selectbox("Convert to", ["PNG", "JPEG"])

    if st.button("Convert", type="primary"):
        suffix = "." + uploaded.name.split(".")[-1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(uploaded.getvalue())
            tmp_path = tmp.name

        out_ext = ".png" if format_choice == "PNG" else ".jpg"
        out_path = tmp_path.rsplit(".", 1)[0] + out_ext

        if format_choice == "PNG":
            success, result = jpeg_to_png(tmp_path, out_path)
        else:
            success, result = png_to_jpeg(tmp_path, out_path)

        if success:
            with open(out_path, "rb") as f:
                out_size = os.path.getsize(out_path) / 1024
                st.success(f"✅ Converted successfully!")
                st.info(f"📦 Original: {file_size:.1f} KB → Converted: {out_size:.1f} KB")
                st.download_button(
                    label="⬇️ Download Converted Image",
                    data=f,
                    file_name=os.path.basename(out_path),
                    mime="image/png" if format_choice == "PNG" else "image/jpeg"
                )
        else:
            st.error(f"❌ Conversion failed: {result}")

        os.remove(tmp_path)
st.divider()

st.markdown("""
## 📌 About Image Formats

### 🔹 PNG (Portable Network Graphics)
PNG is a **lossless format**, meaning it keeps full image quality without losing any data.  
It also supports **transparency**, making it ideal for logos, UI elements, and graphics.

---

### 🔹 JPEG (JPG - Joint Photographic Experts Group)
JPEG is a **lossy format**, which reduces file size by slightly compressing the image.  
It is best suited for **photographs and web images**.

---

## ⚖️ PNG vs JPEG

| Feature        | PNG ✅              | JPEG ✅            |
|---------------|-------------------|-------------------|
| Compression   | Lossless           | Lossy             |
| Quality       | High               | Slightly Reduced  |
| File Size     | Larger             | Smaller           |
| Transparency  | Yes                | No                |

---

## 🚀 How This App Works

1. 📤 Upload your image (JPG, JPEG, or PNG)  
2. ⚙️ The app processes it using Python and Pillow  
3. 🔄 Converts it into your selected format  
4. 📥 Download the converted image instantly  

---

✨ Built for fast, simple, and high-quality image conversion.
""")