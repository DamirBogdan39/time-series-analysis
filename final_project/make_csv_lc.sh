# Create a directory called light_curves
mkdir light_curves

# Copy all files from the kriveu directory to the light_curves directory and add ".csv" to the filenames
for file in kriveu/*; do
    if [ -f "$file" ]; then
        cp "$file" "light_curves/$(basename "$file").csv"
    fi
done

echo "Files copied and renamed successfully!"
