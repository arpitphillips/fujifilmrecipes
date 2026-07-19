#!/usr/bin/env bash
# Fetch the "pending" datasheets from MANIFEST.md into this archive.
#
# Run from this directory on a machine with open network access:
#   bash fetch-datasheets.sh
#
# Direct PDF URLs move over time. Each entry lists the source page next to it;
# when a download 404s, visit the source page and update the URL here.
# Skips anything already downloaded, so it is safe to re-run.

set -u
ok=0; fail=0

get () { # get <dir> <filename> <url>
  local dir="$1" name="$2" url="$3" out
  out="$dir/$name"
  mkdir -p "$dir"
  if [ -s "$out" ]; then echo "skip   $out (exists)"; return; fi
  if curl -fsSL --max-time 90 -A "Mozilla/5.0" -o "$out" "$url" \
     && file "$out" | grep -q PDF; then
    echo "fetch  $out"
    ok=$((ok+1))
  else
    echo "FAIL   $out  <- $url"
    rm -f "$out"
    fail=$((fail+1))
  fi
}

# ---- Kodak motion (source page: https://www.kodak.com/en/motion/products/camera-films/)
get kodak-motion tri-x-reversal_7266.pdf "https://www.kodak.com/content/products-brochures/Film/TRI-X-Reversal-Film-7266-Technical-Data.pdf"
get kodak-motion vision-premier-2393.pdf "https://www.kodak.com/content/products-brochures/Film/kodak-vision-premier-color-print-film-2393.pdf"

# ---- Kodak still, current (source page: https://www.kodakprofessional.com/photographers/technical-resources)
get kodak-still proimage-100_e4039.pdf "https://www.kodakprofessional.com/documents/e4039-pro-image.pdf"

# ---- Kodak still + motion, discontinued (source archive: https://125px.com/docs/film/)
get kodak-still portra-160nc-vc_e190.pdf "https://125px.com/docs/film/kodak/e190-portra160.pdf"
get kodak-still portra-400nc-vc_e191.pdf "https://125px.com/docs/film/kodak/e191-portra400.pdf"
get kodak-still ektachrome-e200_e189.pdf "https://125px.com/docs/film/kodak/e189-ektachromeE200.pdf"
get kodak-still elite-chrome-100_e134.pdf "https://125px.com/docs/film/kodak/e134-elitechrome100.pdf"
get kodak-still verichrome-pan_f7.pdf "https://125px.com/docs/film/kodak/f7-verichromepan.pdf"
get kodak-still panatomic-x_f10.pdf "https://125px.com/docs/film/kodak/f10-panatomicx.pdf"
get kodak-still bw400cn_f4042.pdf "https://125px.com/docs/film/kodak/f4042-bw400cn.pdf"
get kodak-still hie-infrared_f13.pdf "https://125px.com/docs/film/kodak/f13-hie.pdf"
get kodak-motion vision2-500t_5218.pdf "https://125px.com/docs/film/kodak/5218-vision2-500t.pdf"
get kodak-motion vision2-250d_5205.pdf "https://125px.com/docs/film/kodak/5205-vision2-250d.pdf"

# ---- Fujifilm, discontinued (source archive: https://125px.com/docs/film/fujifilm/)
get fujifilm velvia-100f.pdf "https://125px.com/docs/film/fujifilm/velvia100f.pdf"
get fujifilm provia-400x.pdf "https://125px.com/docs/film/fujifilm/provia400x.pdf"
get fujifilm fortia-sp.pdf "https://125px.com/docs/film/fujifilm/fortia-sp.pdf"
get fujifilm sensia-100.pdf "https://125px.com/docs/film/fujifilm/sensia100.pdf"
get fujifilm t64.pdf "https://125px.com/docs/film/fujifilm/t64.pdf"
get fujifilm pro-160ns.pdf "https://125px.com/docs/film/fujifilm/pro160ns.pdf"
get fujifilm superia-200.pdf "https://125px.com/docs/film/fujifilm/superia200.pdf"
get fujifilm superia-800.pdf "https://125px.com/docs/film/fujifilm/superia800.pdf"
get fujifilm superia-1600.pdf "https://125px.com/docs/film/fujifilm/superia1600.pdf"
get fujifilm neopan-400-presto.pdf "https://125px.com/docs/film/fujifilm/neopan400.pdf"
get fujifilm neopan-ss.pdf "https://125px.com/docs/film/fujifilm/neopanss.pdf"
# Current: Acros 100 II (source page: https://asset.fujifilm.com — find via fujifilm.com/us/en/consumer/film)
get fujifilm neopan-acros-100-ii.pdf "https://asset.fujifilm.com/master/emea/files/2020-10/57e5d1e78b1e1f6dc09fca4a90c8f8a1/films_neopan-acros-ii_datasheet_01.pdf"

# ---- Ilford / Harman (source page: https://www.ilfordphoto.com/technical-data/)
get ilford kentmere-pan-200.pdf "https://www.ilfordphoto.com/amfile/file/download/file/2431/product/2126/"

# ---- Foma (source page: https://www.fomafoto.com/en/photographic-films)
get foma fomapan-200.pdf "https://www.fomafoto.com/files/fotografie/cerno-bile-filmy/fomapan-200/fomapan_200_en.pdf"
get foma retropan-320.pdf "https://www.fomafoto.com/files/fotografie/cerno-bile-filmy/retropan-320/retropan_320_en.pdf"
get foma fomapan-r100.pdf "https://www.fomafoto.com/files/fotografie/cerno-bile-filmy/fomapan-r/fomapan_r_100_en.pdf"

# ---- Adox (source page: https://www.adox.de/Photo/adox-films/)
get adox chs-100-ii.pdf "https://www.adox.de/Photo/wp-content/uploads/CHS-100-II-datasheet.pdf"
get adox cms-20-ii.pdf "https://www.adox.de/Photo/wp-content/uploads/CMS-20-II-datasheet.pdf"
get adox hr-50.pdf "https://www.adox.de/Photo/wp-content/uploads/HR-50-datasheet.pdf"

# ---- Rollei / Maco (source page: https://www.macodirect.de — per-film product pages)
get rollei rpx-25.pdf "https://www.macodirect.de/media/pdf/rollei-rpx-25-datasheet.pdf"
get rollei rpx-100.pdf "https://www.macodirect.de/media/pdf/rollei-rpx-100-datasheet.pdf"
get rollei rpx-400.pdf "https://www.macodirect.de/media/pdf/rollei-rpx-400-datasheet.pdf"
get rollei retro-80s.pdf "https://www.macodirect.de/media/pdf/rollei-retro-80s-datasheet.pdf"
get rollei infrared-400.pdf "https://www.macodirect.de/media/pdf/rollei-infrared-400-datasheet.pdf"

# ---- Bergger (source page: https://bergger.com/en/products/pancro-400)
get bergger pancro-400.pdf "https://bergger.com/downloads/pancro400-datasheet-en.pdf"

# ---- Ferrania (source page: https://www.filmferrania.it)
get ferrania p30.pdf "https://www.filmferrania.it/downloads/p30-datasheet.pdf"

echo
echo "done: $ok fetched, $fail failed."
echo "For failures, open the source page in the comment above the entry and update the URL."
echo "Then log new files in README.md and MANIFEST.md (flip pending -> archived)."
