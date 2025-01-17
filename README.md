# Shipping Containers Assets List Management (WIP)
Detection, Identification, and Reporting using YOLO and OCR

## Overview
shipping container asset list management in yard, using YOLO for detection and OCR for identification of container IDs.

## Features
- **Container Detection**: Uses YOLO to locate container IDs in images, even in challenging conditions like obstructions or noisy environments.
- **OCR Integration**: Extracts asset IDs from localized regions using Tesseract or EasyOCR, with error correction for common artifacts.
- **Inventory Reconciliation**: Compares extracted IDs against an inventory list to identify discrepancies (missing or extra containers).
- **Automated Reporting**: Outputs results in CSV format and integrates with platforms like Power BI for visualization.

## Prepared dataset (data folder)
- **Raw containers images**: containers-dataset.zip
- **Cropped containers images not ID-localized for OCR**: cropped_images.zip

## Tool used for dataset sourcing
  [**oneclick-image-downloader-extension**](https://github.com/franklinkemta/oneclick-image-downloader-extension)


## Dataset sourcing references
- https://www.container-xchange.com/blog/container-number/
- https://www.vivacontainers.com/shop/ca/alberta
- https://www.atscontainers.com/en/contact/calgary/
- https://targetbox.ca/product/20ft-shipping-container/
- https://onsitestorage.com/sale-shipping-containers/

## TODO
- Train custom YOLO model for localized container id detection

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
