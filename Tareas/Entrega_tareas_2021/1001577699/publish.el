
;;; publish.el --- Generate Static HTML -*- lexical-binding: t -*-
;;
;; Author: Lincoln Clarete <lincoln@clarete.li>
;;
;; Copyright (C) 2021 Juan David Salcedo
;;
;; This program is free software: you can redistribute it and/or modify
;; it under the terms of the GNU General Public License as published by
;; the Free Software Foundation, either version 3 of the License, or
;; (at your option) any later version.
;;
;; This program is distributed in the hope that it will be useful,
;; but WITHOUT ANY WARRANTY; without even the implied warranty of
;; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
;; GNU General Public License for more details.
;;
;; You should have received a copy of the GNU General Public License
;; along with this program.  If not, see <http://www.gnu.org/licenses/>.
;;
;;; Commentary:
;;
;; How my website is generated!
;;
;;; Code:

(require 'ox-html)
;;(require 'htmlize)

;; Output HTML with syntax highlightng using css classes instead of
;; directly formatting the output.
(setq org-html-htmlize-output-type 'css)

(setq org-publish-project-alist
      '(("posts"
         :base-directory "posts/"
         :base-extension "org"
         :publishing-directory "public/"
         :recursive t
         :publishing-function org-html-publish-to-html
         :auto-sitemap t
         :sitemap-title "Contents"
         :sitemap-filename "index.org"
         :sitemap-style list
         :author "Juan David Salcedo Hernández"
         :email "jdavid.salcedo@udea.edu.co"
         :with-creator t)
        ("obipy-resources"
         :base-directory "posts/obipy-resources/"
         :base-extension "svg"
         :publishing-directory "public/obipy-resources"
         :publishing-function org-publish-attachment
         :recursive t)
         ("all" :components ("posts" "obipy-resources"))))

;;; publish.el ends here
